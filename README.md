<a id="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Brandon-Cole/Good_News_Bad_News">
    <img src="data/JJ.jpg" alt="Logo" style="width:1500%; height:auto;">
  </a>

<h3 align="center"><strong>Project Title</strong></h3>

<p align="center">
    <em>“The duty of a journalist is to write the truth. Journalism means you go back to the actual facts, you look at the documents, you discover what the record is, and you report it.”</em> – <strong>Noam Chomsky</strong>
</p>

<p align="center">
    Humans have imperfect memories and can be easily biased when taking in new information. As it turns out, much of the interpretation of a news article begins at the headline. Multiple studies have shown that headlines affect the reader's recall and interpretation of the news reported.<sup>1</sup>,<sup>2</sup> 
</p>

<p align="center">
    To this end, I sought to investigate the extent of the headline:article relationship using natural language processing.
</p>

<p align="center">
    <strong>References:</strong><br>
    1. Ecker, U. K. H., Lewandowsky, S., Chang, E. P., & Pillai, R. (2014). The effects of subtle misinformation in news headlines. Journal of Experimental Psychology: Applied, 20(4), 323–335. https://doi.org/10.1037/xap0000028<br>
    2. Digirolamo, G.J., Hintzman, D.L. First impressions are lasting impressions: A primacy effect in memory for repetitions. Psychonomic Bulletin & Review 4, 121–124 (1997). https://doi.org/10.3758/BF03210784
</p>



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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Good News Bad News (GNBN) is a natural language processing project intended to investigate the magnitude of bias introduced by news headlines.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

<ul>
  <li><a href="https://www.docker.com/" target="_blank"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"></a></li>
  <li><a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"></a></li>
  <li><a href="https://pytorch.org/" target="_blank"><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="PyTorch"></a></li>
  <li><a href="https://scikit-learn.org/" target="_blank"><img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"></a></li>
  <li><a href="https://www.tensorflow.org/" target="_blank"><img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="TensorFlow"></a></li>
  <li><a href="https://pandas.pydata.org/" target="_blank"><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"></a></li>
  <li><a href="https://numpy.org/" target="_blank"><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"></a></li>
  <li><a href="https://matplotlib.org/" target="_blank"><img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib"></a></li>
</ul>


<!-- GETTING STARTED -->
## Getting Started

I build my container with:
docker build . -t GNBN

Run container with:
docker run -p 8787:8787 -it --rm -e PASSWORD=mypassword GNBN

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Contributors:

<a href="https://github.com/Brandon-Cole/Good_News_Bad_News/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Brandon Novy - [@twitter_handle](https://twitter.com/twitter_handle) - novy@unc.edu

Project Link: [https://github.com/Brandon-Cole/Good_News_Bad_News](https://github.com/Brandon-Cole/Good_News_Bad_News)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Brandon-Cole/Good_News_Bad_News.svg?style=for-the-badge
[contributors-url]: https://github.com/Brandon-Cole/Good_News_Bad_News/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Brandon-Cole/Good_News_Bad_News.svg?style=for-the-badge
[forks-url]: https://github.com/Brandon-Cole/Good_News_Bad_News/network/members

[stars-shield]: https://img.shields.io/github/stars/Brandon-Cole/Good_News_Bad_News.svg?style=for-the-badge
[stars-url]: https://github.com/Brandon-Cole/Good_News_Bad_News/stargazers

[issues-shield]: https://img.shields.io/github/issues/Brandon-Cole/Good_News_Bad_News.svg?style=for-the-badge
[issues-url]: https://github.com/Brandon-Cole/Good_News_Bad_News/issues

[license-shield]: https://img.shields.io/github/license/Brandon-Cole/Good_News_Bad_News.svg?style=for-the-badge
[license-url]: https://github.com/Brandon-Cole/Good_News_Bad_News/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/brandon-novy-5a4227263/

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/

[PyTorch]: https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white
[PyTorch-url]: https://pytorch.org/

[scikit-learn]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[scikit-learn-url]: https://scikit-learn.org/

[TensorFlow]: https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/

[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/

[NumPy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org/