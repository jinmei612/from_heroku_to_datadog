# Overview
- Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

- Datadog is a Service as a service (SaaS) monitoring and analytics tool that can be used to monitor your heroku applications.

This repo will show you how to monitor the performance of your Heroku webapp in Datadog.


# Getting Started
- Sign up for a free Heroku account: https://www.heroku.com/pricing 
- Sign up for a free Datadog account: https://www.datadoghq.com/pricing/ 


# Create Heroku Project
- Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

- Run `heroku login` to login in your terminal

- Run the following in your terminal to create a new Heroku project (You can also go to your [heroku dashboard](https://dashboard.heroku.com/apps) and click `New` -> `Create new app` to create a new project)

```
mkdir your-heroku-project
cd your-heroku-project
heroku create
git init
```

Sample output:
```
> heroku create
Creating app... done, ⬢ gentle-plains-40923
https://gentle-plains-40923.herokuapp.com/ | https://git.heroku.com/gentle-plains-40923.git
```

- Switch to your project by running `heroku git:remote -a <your-heroku-project-name>`

Sample output:
```
> heroku git:remote -a gentle-plains-40923
set git remote heroku to https://git.heroku.com/gentle-plains-40923.git
```


- This app is written in Python, so we are going to add the language buildpack by running `heroku buildpacks:add heroku/python`

Sample Output:
```
> heroku buildpacks:add heroku/python
Buildpack added. Next release on gentle-plains-40923 will use heroku/python.
Run git push heroku master to create a new release using this buildpack.
```


- Enable Heroku Labs Dyno Metadata by running `heroku labs:enable runtime-dyno-metadata -a $(heroku apps:info|grep ===|cut -d' ' -f2)`

Sample Output:
```
> heroku labs:enable runtime-dyno-metadata -a $(heroku apps:info|grep ===|cut -d' ' -f2)
Enabling runtime-dyno-metadata for gentle-plains-40923... done
```

# Use Datadog To Monitor Heroku App

- Now add the monitoring buildpack Datadog by runnning `heroku buildpacks:add https://github.com/DataDog/heroku-buildpack-datadog.git`

Sample output:
```
> heroku buildpacks:add https://github.com/DataDog/heroku-buildpack-datadog.git
Buildpack added. Next release on gentle-plains-40923 will use:
  1. heroku/python
  2. https://github.com/DataDog/heroku-buildpack-datadog.git
Run git push heroku master to create a new release using these buildpacks.
```


- Note down your Datadog API key: https://app.datadoghq.com/account/settings#api (create a new one if you don't have one yet.)
Set your datadog api key in your project and make sure you have `DD_DYNO_HOST` set to true and that `HEROKU_APP_NAME` has a value set for every Heroku application 


`heroku config:add DD_API_KEY=<your_own_api_key_here>`

`heroku config:add DD_DYNO_HOST=true`



`heroku config:add HEROKU_APP_NAME=<your-app-name>` (run `heroku config`, if `HEROKU_APP_NAME` is already set, skip this step)



Sample output:
```
> heroku config:add DD_API_KEY=<your_own_api_key_here>
Setting DD_API_KEY and restarting ⬢ gentle-plains-40923... done, v3
DD_API_KEY: <your_own_api_key_here>
```

- Set datadog env tag for the host and APM environment 

`heroku config:add DD_TAGS="env:heroku"`

`heroku config:add DD_APM_ENV=heroku`

Sample Output:
```
> heroku config:add DD_TAGS="env:heroku"
Setting DD_TAGS and restarting ⬢ gentle-plains-40923... done, v10
DD_TAGS: env:heroku
```

- `cd` into your Heroku project directory and download the files in this repo (app.py, Procfile, requirements.txt, runtime.txt). (Optionally, you can also include  `datadog/config.d/http_check.yaml` in your project which enables the http_check integration: [doc](https://github.com/DataDog/heroku-buildpack-datadog#enabling-integrations))


- Deploy your Heroku app (be patient, it takes time)

```
git add .
git commit -am "make it better"
git push heroku master
```

- `curl <your-app-url>` to generate some `bubble_tea.*` metrics and traces

- Now go into your Datadog account and check the performance of your application and dyno

  https://app.datadoghq.com/infrastructure 

  https://app.datadoghq.com/apm/services

- It's time to be creative now! 
  Here is a sample dashboard that helps me to decide which bubble tea to order for the day.

  https://p.datadoghq.com/sb/4d8a719d2-b022699bae85db7f21832d76b34d1f4f 



# Reference:

https://docs.datadoghq.com/agent/basic_agent_usage/heroku/ 

https://github.com/DataDog/heroku-buildpack-datadog

https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true

