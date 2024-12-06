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

<h3 align="center"><strong>Good News Bad News: An AI-Driven News Study</strong></h3>

<p align="center">
    <em>“The duty of a journalist is to write the truth. Journalism means you go back to the actual facts, you look at the documents, you discover what the record is, and you report it.”</em> – <strong>Noam Chomsky</strong>
</p>

<p>
    Humans have imperfect memories and can be easily biased when taking in new information. As it turns out, much of the interpretation of a news article begins at the headline. Multiple studies have shown that headlines affect the reader's recall and interpretation of the news reported.<sup>1</sup>,<sup>2</sup> To this end, I sought to investigate the extent of the headline:article relationship using natural language processing.
</p>

<p align="center">
    <strong>References:</strong><br>
    1. Ecker, U. K. H., Lewandowsky, S., Chang, E. P., & Pillai, R. (2014). The effects of subtle misinformation in news headlines. Journal of Experimental Psychology: Applied, 20(4), 323–335. https://doi.org/10.1037/xap0000028<br>
    2. Digirolamo, G.J., Hintzman, D.L. First impressions are lasting impressions: A primacy effect in memory for repetitions. Psychonomic Bulletin & Review 4, 121–124 (1997). https://doi.org/10.3758/BF03210784
</p>


<div align="center">
  <h3>Built With</h3>
  <a href="https://www.docker.com/" target="_blank">
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  </a>
  <br>
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  </a>
  <br>
  <a href="https://pytorch.org/" target="_blank">
    <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="PyTorch">
  </a>
  <br>
  <a href="https://scikit-learn.org/" target="_blank">
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  </a>
  <br>
  <a href="https://www.tensorflow.org/" target="_blank">
    <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="TensorFlow">
  </a>
  <br>
  <a href="https://pandas.pydata.org/" target="_blank">
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  </a>
  <br>
  <a href="https://numpy.org/" target="_blank">
    <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  </a>
  <br>
  <a href="https://matplotlib.org/" target="_blank">
    <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib">
  </a>
</div>


<!-- GETTING STARTED -->
## Getting Started

I built my container with:

  ```sh
docker build . -t GNBN
```

Run container with:
 ```sh
docker run -p 8787:8787 -it --rm -e PASSWORD=mypassword GNBN
```

<!-- USAGE EXAMPLES -->
## Reproducibility

To perform the analysis shown here, you can run the Makefile provided which should assemble the report and database. I have also included the LLM scripts which were run on a HPC cluster due to resource limitations.

_To directly view the analytical report please visit [Web Report](https://brandon-cole.github.io/Good_News_Bad_News/)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Future Directions

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Brandon Novy - [@Linkedin](https://www.linkedin.com/in/brandon-novy-5a4227263/) - novy@unc.edu

Web Link: [https://github.com/Brandon-Cole/Good_News_Bad_News](https://brandon-cole.github.io/Good_News_Bad_News/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Dr. Vincent Toups for his guidance and support

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