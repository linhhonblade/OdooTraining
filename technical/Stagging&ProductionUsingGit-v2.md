If you are running a large project such as a website or ansible server you will want to test new features before pushing them into production then something like the following setup may work for you.

For this example imagine your url is mysite.ca and you want a development/staging site on a subdomain which is dev.mysite.ca

# Setup

## For websites

Create the website's domain and subdomain

    mysite.ca
    dev.mysite.ca

## On remote server

### connect

    ssh username@ipaddress

## Create the main repo

    mkdir ~/projects/ace/
    git init --bare workstation_parc

Alternativly

    git init --bare mysite.ca

## clone your new main repo to your local machine.

    git clone ssh://username@server_ip/~/projects/ace/mysite.ca

This repo will be used for version control only. See the **workflow** section for usage once we setup all the repos required.

## Connect to the server

    ssh username@server_ip

### create a staging repo

    cd ~/projects/ace
    git init --bare staging.mysite.ca

## create a production repo

    git init --bare production.git

You should now have 3 repos on the server and 1 local clone.

## deployment hooks

Next we setup some hooks that will be used to automatically populate the staging and production directories.

### Create staging repo hook.

The staging hook will automatically pull and checkout the latest version of your website in the dev folder.

    cd ~/projects/ace/staging.mysite.ca/hooks
    post-receive
    nano post-receive

#### Content example

  * #!/bin/sh
  * GIT_WORK_TREE=../../dev git checkout -f master

#### ensure permissions

Since the hook is a bash script we need to ensure that it is executable.

    chmod a+x post-receive

##### related man excerpt

    A  combination  of the letters ugoa controls which users' access to the
    file will be changed: the user who owns it  (u),  other  users  in  the
    file's group (g), other users not in the file's group (o), or all users
    (a).  If none of these are given, the effect is as if a were given, but
    bits that are set in the umask are not affected.

    The  operator  +  causes the selected file mode bits to be added to the
    existing file mode bits of each file; - causes them to be removed;  and
    =  causes  them  to  be added and causes unmentioned bits to be removed
    except that a directory's unmentioned set user and group  ID  bits  are
    not affected.

### setup the production repo hook

The production hook will be slightly different as it will deploy to the production website folder.

    cd ~/projects/ace/production.mysite.ca/hooks
    post-receive
    nano post-receive

#### Content example

    #!/bin/sh
    GIT_WORK_TREE=../../httpdocs git checkout -f master

#### ensure permissions

Since the hook is a bash script we need to ensure that it is executable.

    chmod a+x post-receive

## Local workstation repo

On your local clone we will add two of the remote repositories

    git remote add staging username@ipaddress/~/private/staging.git
    git remote add production username@ipaddress/~/private/production.git

and that is it.

## Standard Workflow

We have three repos setup on our server. Our main repository along with one for staging and one for production

When developing on your workstation you will push every commit to the main repo in order to ensures that all commits are saved in a single repository.

### pushing to the master

AFter making change on your local clone you runn the following:

    git add --all
    git commit -m 'added some awesome new features'
    git push origin master

`git push origin master` saves all changes to the main repo on the server but **does not ever deploy any code** as the main repository is used for version control only.

### pushing to staging

When you want to test the changes made to your main repository you push them to the staging staging (dev.mysite.ca) repository run the following:

    git push staging master

The staging hook will be initiated and will automatically checkout these new files into the dev folder.

### pushing to production

After intense testing on the staging server and once your changes are ready to be deployed to the producton server you would run something like the following:

    git push production master

The production hook will be initiated and all of the changes made will end up in the web (httpdocs) folder or other type of server's folder and will be live!

### IMPORTANT

So, as long as you push to origin first everytime you make changes, all other developers working on the same site or server will be able to pull your work keeping everyone on the same page.
