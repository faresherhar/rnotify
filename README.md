<h1 align="center">Rnotify</h1>

<h2 align="center">The Repository Releases Tracker</h2>

<p align="center">
  <a href="https://www.python.org/"><img alt="Supported Python Versions: 3.12" src="https://img.shields.io/badge/python-3.12-blue?logo=python"></a>
  <a href="https://pypi.org/project/pip/"><img alt="Pip Version: v24.0" src="https://img.shields.io/pypi/v/pip?logo=Pypi"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

> Up-to-date to the latest release of your favorite opensource tools.”

**Rnotify**, is a Python tool for tracking releases. By using it, you are notified of the latest release of your configured repositories. It uses the Github, and Gitlab APIs to scrape the data of the releases related to your repositories, and sends you a message to notify you of the latest release, by Email.

For more details, installation instrucions, and configuration, please refer to the documentation below.

## Documentation

- [Contributing](./doc/CONTRIBUTING.md)
- [Installation](./doc/INSTALLATION.md)

## FAQ

> Why building Rnotify ?

At the time, I worked within a team, in which our technical environment heavily depends on open source projects, and we had many tools that were outdated. Being unable to track the new releases of each single opensource application, was the reason for it.

Thus, I created Rnotify, to do the job for us. A backend application, that keeps us updated with the new releases.

> What are the supported developer platforms ?

At the moment, the application supports only the Github, and the Gitlab APIs. However, if there's the need to support another platform, please open an issue for it, or add it yourself, and open a pull request.

> Do I need API keys for using Rnotify ?

It is not mendatory to provide any API keys. Still, both the Github, and Gitlab APIs, have some limitations without the API keys. The short answer is, unless you have too many repositories listed, or doing checks on a hourly basis, the application still works fine, without the API keys.

Please take adeeper look at the documentation [Github Rate Limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28), [Gitlab Rate Limits](https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits).

> What are the notification services supported ?

The application was designed to send notifications via emails only. This doesn't eliminate the chanse to adding more services in the future.

> Can I change the HTML template for the notification ?

Yes totally. Create your own HTML template, whilst respecting the data fields, and the Jinja syntax.

> How can I run Rnotify ?

Rnotify, was designed with containers in mind. A Helm Chart is provided alongside the project, kubernetes is the main deployment enviroment. You can still run it, on any system that supports containers, even without having Kubernetes.