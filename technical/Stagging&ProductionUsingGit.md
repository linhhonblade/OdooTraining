# Stagging & Production Using Git
If you are running a large website where you will need to test new features on a seperate url before pushing them live then the following instructions are for you ;)

For this example imagine your url is `apple.com` and you want a development/staging site on a subdomain which is `dev.apple.com`

## Setup

1. First thing you'll want to do is go ahead and create your website in Plesk and add the subdomain `dev.apple.com` at the same time.
2. ssh into the server e.g. `$ ssh username@ipaddress`
3. Once logged in cd into the private directory (this will be where all git repos are stored) e.g. `$ cd ~/private`
4. Create the main repo e.g. `$ git init --bare apple.git`
5. Now to clone this new repo on your local machine.`$ git clone ssh://username@ipaddres/~/private/apple.com`
6. This repo will be simply for version control only, I will explain workflow after we have setup each required repo.
7. On the server in the private directory create a new repo named staging e.g. `$ git init --bare staging.git`
8. Once the staging directory is create do the exact same for production e.g. `$ git init --bare production.git`
9.  You will now have 3 repos on the server and 1 local clone.
10. Now it's time to setup some deployment hooks (these will be used to automatically deploy to a specific directory).
11. Lets add a hook to the staging repo. cd into the `staging.git` folder and then into the folder called hooks e.g. `cd staging.git/hooks`
12. Once in the hook folder we will need to either create or edit the file named `post-receive` run the following cmd: `$ touch post-receive`
13. Now to edit that file run: `$ nano post-receive` and enter the following:
  * `#!/bin/sh`
  * `GIT_WORK_TREE=../../dev git checkout -f master`
14. This hook tells the repo to automatically pull and checkout the latest version of your website in the dev folder. WE'll talk about how initiate this hook soon.
15. To save that edit do a `Control-X`, hit `Y` and then `Enter`.
16. Now we need to do exactly the same for the `production.git` repo except the hook will be slightly different (it will deploy to the live website not the dev folddirer).
17. The contents of the `post-receive` file in the production repo should be:
    * `#!/bin/sh`
    * `GIT_WORK_TREE=../../httpdocs git checkout -f master`
18. To ensure you run into no permission issues run this command on each of those files: `$ chmod a+x post-receive`
19. On your local copy you will need to add the following lines so your local repo knows where each repo is:
    * `$ git remote add staging username@ipaddress/~/private/staging.git`
    * `$ git remote add production username@ipaddress/~/private/production.git`
20. And you're done! I will explain how this works in your everyday workflow below.

## Workflow
Ok so we have these 3 repos setup e.g. staging.git, production.git and apple.git, now what do I do?

So basically every commit you do will need to be pushed to the main repo (This ensures all commits are saved in one place) for example say I just added some new files, i'd then need to run:
  1. `$ git add --all`
  2. `$ git commit -m "added some awesome new features"`
  3. `$ git push origin master`
This saves the changes but doesn't actually get deployed (EVER), as said previously it's simply for version control.
Now lets say I want those new files pushed to the staging (`dev.apple.com`) repo, id' run this:
  1. `$ git push staging master`
The hook we setup will now be initiated and will automatically checkout these new files into the dev folder. Awesome right?
Now after some intense testing on the those new files we just added lets say were now ready to deploy... we'd run:
  1. `$ git push production master`
The hook for that repo will be initiated and now all changes made are in the httpdocs folder and will be live!

Now as long as you remember to push to origin first all other developers working on the same site will be able to pull your work. This way everybody is on the same page.

