
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<br />
<div align="center">
  <a href="https://github.com/anaghpatel/LibRizz-2.0">
    
  </a>

<h3 align="center">LibRizz 2.0</h3>

  <p align="center">
    Dockerized Version of Automatic library room booking bot for Springshare Libcal
    <br />
    <br />
    <a href="https://github.com/anaghpatel/LibRizz-2.0/issues">Report Bug</a>
    

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<!-- ADD INFO ABOUT THE PROJECT -->
<!--[![Product Name Screen Shot][product-screenshot]]-->


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![ENV][.ENV-shield]][.ENV-url]
* [![Awesome-Lists][Awesome-Lists-shield]][Awesome-Lists-url]
* [![Docker][Docker-shield]][Docker-url]
* [![Python][Python-shield]][Python-url]
* [![Selenium][Selenium-shield]][Selenium-url]



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is my first docker project.so bear with me.
To get a local copy up and running follow these simple example steps.

### 👨‍🍳 Prerequisites

As this is docker project you need to have docker desktop installed on your device to spin up build image and spin up the containers.You can use guide on Website below set up docker desktop based on your host operating system.
* Docker Desktop
  ```sh
  https://docs.docker.com/desktop/
  ```

### 🤸 Installation

_Once you have Docker installed you can folow the steps below to spin up the required docker containers._
1. Clone the repo
   ```sh
   git clone https://github.com/anaghpatel/LibRizz-2.0.git
   ```
2. Open CMD or bash shell in cloned repo. 
<br />

3. Pull Selenium chrome standalone docker image rom Docker Hub
  _`Normal Version`_
   ```sh
   docker pull selenium/standalone-chrome
   ```
   I am hosting this project in raspberry pi so I used arm version 
   _`Arm Version`_
   ```sh
   docker pull seleniarm/standalone-chromium
   ```
<br />

4. Once you pull image, change `driver_ip` in `LibRizz.py` to any ip address that you want as long as its not in use in your network. I am going with `http://172.17.0.2` and by default we are using port `4444` for selenium webdriver.

<br />

5. It is time to build docker image using docker file. Run this command from same directory as dockerfile 
   ```sh
   docker build -t librizz:1.0 .
   ```

<br />

6. Using comand below spin up the Selenium container
  _`Normal Version`_
   ```sh
   docker run --rm -d -it --name TempSelenium --ip="172.17.0.2" -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium/standalone-chrome:latest sh
   ```
   _`Arm Version`_
   ```sh
   docker run --rm -d -it --name TempSelenium  --ip="172.17.0.2" -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g seleniarm/standalone-chromium:latest
   ```

<br />

7. Run the LibRizz Container using command below. (This commad fires up LibRizz.py that makes the reservation automatically. )
   ```sh
   docker run -d --rm --shm-size="2g" --name LibRizz librizz:1.0

   ```
 
<br />

8. Last and final step is to stop Selenium container. (LibRizz container self-destroys itself once its finished running script.)
   ```sh
   docker stop TempSelenium

   ```



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## 🔎 Usage

Main usage of this project is automatically reserving library room at any instituation that uses LibCal by SpringShare. The automation script to reserve room is more focused on UCF's Version of LibCal but can be modified to any Instituation's LibCal.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## 🗺 Roadmap

- [x] Write Installation Instruction 
- [ ] Add MultiThreading
- [ ] Write Powershell to automatically execute all commands
    - [ ] Use Windows Scheduler/Crontab to schedule this script to run at specific time

See the [open issues](https://github.com/anaghpatel/LibRizz-2.0/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

```text
The MIT License (MIT)
Copyright (c) 2024 Anagh Patel
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## 📧 Contact

Anagh Patel - [@anagh_patel](https://twitter.com/anagh_patel) - anaghpatel28@gmail.com

Project Link: [https://github.com/anaghpatel/LibRizz-2.0](https://github.com/anaghpatel/LibRizz-2.0)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## 🙏 Acknowledgments

* [Img Shields](https://shields.io)
* [Font Awesome](https://fontawesome.com)
* [This Amazing Template](https://github.com/othneildrew/Best-README-Template)
* [Seleniumarm Docker](https://github.com/seleniumhq-community/docker-seleniarm)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/anaghpatel/LibRizz-2.0.svg?style=for-the-badge
[contributors-url]: https://github.com/anaghpatel/LibRizz-2.0/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/anaghpatel/LibRizz-2.0.svg?style=for-the-badge
[forks-url]: https://github.com/anaghpatel/LibRizz-2.0/network/members
[stars-shield]: https://img.shields.io/github/stars/anaghpatel/LibRizz-2.0.svg?style=for-the-badge
[stars-url]: https://github.com/anaghpatel/LibRizz-2.0/stargazers
[issues-shield]: https://img.shields.io/github/issues/anaghpatel/LibRizz-2.0.svg?style=for-the-badge
[issues-url]: https://github.com/anaghpatel/LibRizz-2.0/issues
[license-shield]: https://img.shields.io/github/license/anaghpatel/LibRizz-2.0.svg?style=for-the-badge
[license-url]: https://github.com/anaghpatel/LibRizz-2.0/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/anpatel
[product-screenshot]: images/screenshot.png
[.ENV-shield]: https://img.shields.io/badge/.ENV-222222?style=for-the-badge&logo=.ENV&logoColor=ECD53F
[.ENV-url]: https://pypi.org/project/python-dotenv/
[Awesome-Lists-shield]: https://img.shields.io/badge/Awesome%20Lists-FC60A8?style=for-the-badge&logo=Awesome+Lists&logoColor=FFFFFF
[Awesome-Lists-url]: https://github.com/othneildrew/Best-README-Template
[Docker-shield]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=FFFFFF
[Docker-url]: https://www.docker.com/
[Python-shield]: https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=Python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Selenium-shield]: https://img.shields.io/badge/Selenium-%43B02A?style=for-the-badge&logo=Selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/
