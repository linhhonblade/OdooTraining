# Overview

The JS Framework is designed to work with 3 main use cases:
- the web client: private web client
- the website: public part of odoo
- the point of sale: a specialized single page application

This document will focus mostly on the web client design

# Web Client
## Single Page Application

In short, the webClient, instance of WebClient is the root component of the whole user interface.

In runtime, the web client is a single page application. It does not need to request a full page from the server each time the user perform an action. Instead, it only requests what it needs, and then replaces/updates the view.

## Overview of the web client JS code

The web client code, in the `web/static/src/js` addon
- `boost.js`: defines the module system, it needs to be loaded first
- `core/`: it contains the class system, the widget system, concurrency utilities, and many other class/functions.
- `chrome/`: it has most large widgets which make up most of the user interface.
- `chrome/abstract_web_client.js` and `chrome/web_client.js`: define the WebClient widget, which is the root widget for the web client
- `chrome/action_manager.js`: the code convert action to widget
- `fields/`: all main view field widgets
- `views/`: this is where views are located

## Asset Management

- We define a set of bundles in xml (a bundle is a collection of files: js, css, scss)
- The most important bundles are defined in file `addons/web/views/webclient_templates.xml`
