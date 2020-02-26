# Overview
- Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

- Datadog is a Service as a service (SaaS) monitoring and analytics tool that can be used to monitor your heroku applications.

This repo will show you how to send metrics and traces from your heroku app to datadog


# Getting Started
- Sign up for a free Heroku account: https://www.heroku.com/pricing 
- Sign up for a free Datadog account: https://www.datadoghq.com/pricing/ 


# Create Heroku Project
- You can go to your [heroku dashboard](https://dashboard.heroku.com/apps) and click `New` -> `Create new app`, or run `heroku create` in your terminal to create a new Heroku project (Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line))

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

* Use Datadog To Monitor Heroku App

- Now add the monitoring buildpack Datadog by runnning `heroku buildpacks:add https://github.com/DataDog/heroku-buildpack-datadog.git`

Sample output:
```
> heroku buildpacks:add https://github.com/DataDog/heroku-buildpack-datadog.git
Buildpack added. Next release on gentle-plains-40923 will use:
  1. heroku/python
  2. https://github.com/DataDog/heroku-buildpack-datadog.git
Run git push heroku master to create a new release using these buildpacks.
```


- Note your Datadog API KEY: https://app.datadoghq.com/account/settings#api create a new one if you don't have one yet.
Set your datadog api key in your project by running. Make sure you have `DD_DYNO_HOST` set to true and that `HEROKU_APP_NAME` has a value set for every Heroku application 

`heroku config:add DD_API_KEY=<your_own_api_key_here>`
`heroku config:add DD_DYNO_HOST=true`
`heroku config:add HEROKU_APP_NAME=<your-app-name>`


Sample output:
```
> heroku config:add DD_API_KEY=<your_own_api_key_here>
Setting DD_API_KEY and restarting ⬢ gentle-plains-40923... done, v3
DD_API_KEY: <your_own_api_key_here>
```

- Set datadog env tag for the host and APM environment 
`heroku config:add DD_TAGS="env:heroku_datadog"`

Sample Output:
```
> heroku config:add DD_TAGS="env:heroku_datadog"
Setting DD_TAGS and restarting ⬢ gentle-plains-40923... done, v10
DD_TAGS: env:heroku
```

- `cd` into your Heroku project directory and download the files in this repo (app.py, Procfile, requirements.txt, runtime.txt). (Optionally, you can also include the `datadog` folder in your project which enable integrations: [doc](https://github.com/DataDog/heroku-buildpack-datadog#enabling-integrations))


- Deploy your Heroku app (be patient, it takes some time)

```
git add .
git commit -am "make it better"
git push heroku master
```


Reference:

https://docs.datadoghq.com/agent/basic_agent_usage/heroku/ 

https://github.com/DataDog/heroku-buildpack-datadog

https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true
