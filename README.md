# COMP 3122 - Python AI/ML class
 * [Course outline on GBC website](https://www.georgebrown.ca/CO/gbc/technology/school-of-computer-technology/courses/COMP/3122/COMP-3122-T127.html) (older outline draft as [md file](Outline.md))
 * Slack signup page - https://join.slack.com/t/georgebrowntech/signup
 
## Book
Python Data Science Handbook: Essential Tools for Working with Data (by Jake VanderPlas)  
- [Read online](https://jakevdp.github.io/PythonDataScienceHandbook/)
- GitHub repository: https://github.com/jakevdp/PythonDataScienceHandbook

## Tools
 - Anaconda download page: https://www.anaconda.com/download/ (Use the Python 3.6 version)
 - Basic tutorial about git and GitHub: [video](https://www.youtube.com/watch?v=0fKg7e37bQE) (skip it if you used git before)

## Prerequisites
This course assumes reasonable knowledge of Python, if you haven't used Python before, consider one of the following resources:
- [Codecademy's Python course](https://www.codecademy.com/learn/learn-python) - browser-based, tons of exercises
- [DataQuest](https://www.dataquest.io/) - browser-based, teaches Python in the context of data science
- [CheckIO](https://checkio.org/) - a good collection of exercises to try when you are comfortable with the basics

## Week 1
   * [Lab notebook - Sept 4th](lectures/01_week_lab.ipynb)
   * [Lecture notebook - Sept 6th](lectures/01_week.ipynb)
   * Recommended Video: [Making data mean more through storytelling](https://www.youtube.com/watch?v=6xsvGYIxJok) by Ben Wellington at TEDxBroadway (15 min)
   
## Week 2
 * Lab - Sept 11
   * Lab exercise - [exercises/numpy_basics.ipynb](exercises/numpy_basics.ipynb)
     * [Solutions](http://nbviewer.jupyter.org/url/kamrik.org/ML1/numpy_basics_solutions.ipynb)
   * [Slides](lectures/02_week_lab.ipynb)
 * Lecture - Sept 13
   * [Slides](lectures/02_week.ipynb) (not too many of them, most of the lecture is live / whiteboard) 
   * [Whiteboard screenshot](lectures/02_week_whiteboard.png) (png image, for full resolution click "Download" above the image)
   * [IPython transcript](lectures/02_week_ipython_transcript.py) (What the instrucor was typing - no output. Not usefully runnable as a single Python file)
 * Links
   * NumPy
     * Quick reference: https://github.com/juliangaal/python-cheat-sheet
     * Videos: [video 1](https://www.youtube.com/watch?v=BLGo3PXoX1A), [video 2](https://www.youtube.com/watch?v=7YvKhcs7sb0) - from the [Python Programmer YouTube channel](https://www.youtube.com/channel/UC68KSmHePPePCjW4v57VPQg)
   * Matplotlib
     * A [playlist of several good short videos introducing different types of plots with matplotlib](https://www.youtube.com/watch?v=zl5qPnqps8M&index=2&list=PLeo1K3hjS3uu4Lr8_kro2AqaO6CFYgKOl) This link skips the first video in the playlist because it talks about installation and you already have matplotlib installed via Anaconda.
     * [Basic plotting tutorial on matplotlib website](https://matplotlib.org/users/pyplot_tutorial.html)
   * [Facts and Myths about Python names and values](https://www.youtube.com/watch?v=_AEJHKGk9ns) - by Ned Batchelder at PyCon 2015 (video, 25min)
 
   
## Week 3
 * Lab - Sept 18
   * [Slides](lectures/03_week_lab.ipynb)
   * Lab exercise - [exercises/plotting_basics.ipynb](exercises/plotting_basics.ipynb) (it uses [exercises/OshawaWeather2016.csv](exercises/OshawaWeather2016.csv))
     * [Solutions](http://nbviewer.jupyter.org/url/kamrik.org/ML1/plotting_basics_solutions.ipynb)
 * Lecture - Sept 20
   * [Slides](lectures/03_week.ipynb)
 * Home reading & videos (important!)
   * [Video playlist about Pandas](https://www.dataschool.io/easier-data-analysis-with-pandas/) (watch the first 10 videos - about 1 hour 33 min total)
   * [Notebook & data used in the videos](https://github.com/justmarkham/pandas-videos/) (GitHub) - the notebook has sufficient comments to be very useful without videos as well
   
## Week 4
 * Home assignment - [exercises/numpy_assignment.py](exercises/numpy_assignment.py) (instructions inside)
 * Lab - Sept 25
   * [Slides](lectures/04_week_lab.ipynb)
   * Lab exercise - [exercises/olympic_history.ipynb](exercises/olympic_history.ipynb)
     * Solutions - [exercises/olympic_history_solutions.ipynb](exercises/olympic_history_solutions.ipynb)
 * Lecture - Sept 27
   * [Slides](lectures/04_week.ipynb)
 * More videos about Pandas
   * [Pandas best practices](https://www.youtube.com/playlist?list=PL5-da3qGB5IBITZj_dYSFqnd_15JgqwA6) - video playlist

## Week 5
 * Lab - Oct 2
   * [Slides](lectures/05_week_lab.ipynb)
   * Exercise: [exercises/active_satellites.ipynb](exercises/active_satellites.ipynb) and  [exercises/active_satellites.csv](exercises/active_satellites.csv)
     * [Solutions](http://nbviewer.jupyter.org/url/kamrik.org/ML1/active_satellites_solutions.ipynb)
 * Lecture - Oct 4
   * [Slides](lectures/05_week.ipynb)
   
## Week 6
 * [Home Assignment 1](exercises/numpy_assignment.py) is due Tuesday Oct 9, 23:59
 * Lab - Oct 9
   * [Slides](lectures/06_week_lab.ipynb)
   * Exercise: [exercises/week6_lab.ipynb](exercises/week6_lab.ipynb)
     * [Solutions](http://nbviewer.jupyter.org/url/kamrik.org/ML1/week6_lab_solutions.ipynb)
 * Lecture - Oct 11
   * [Slides](lectures/06_week.ipynb)
## Week 7
 * Lab - Oct 16
 * Lecture - Oct 18, MID-TERM
## Week 8 - Intersession Week (Oct 22-28)

# Part 2 - scikit-learn
 * scikit-learn is already installed if you use Anaconda Python
 * [Video playlist](https://www.dataschool.io/machine-learning-with-scikit-learn/) and [corresponding notebooks](https://github.com/justmarkham/scikit-learn-videos)  (**highly recommended**)
   * Skim through this [post about changes in scikit-learn since the videos were recorded](https://www.dataschool.io/how-to-update-your-scikit-learn-code-for-2018/)
 * Book [chapter 5](https://jakevdp.github.io/PythonDataScienceHandbook/#5.-Machine-Learning)
  
## Week 9
 * Lab - Oct 30
   * [Slides](lectures/09_week_lab.ipynb)
   * Exercise: [exercises/mpg_regression.ipynb](exercises/mpg_regression.ipynb)
 * Lecture - Nov 1
   * [Slides](lectures/09_week.ipynb) (alternative link [via nbviewer](http://nbviewer.jupyter.org/github/kamrik/ML1/blob/master/lectures/09_week.ipynb))
   * [Whiteboard screenshot](lectures/knn_whiteboard.png)
 * Links
   * [So Why Is It Called "Regression," Anyway?](http://blog.minitab.com/blog/statistics-and-quality-data-analysis/so-why-is-it-called-regression-anyway)
   * [Linear regression example - Boston housing dataset](https://www.youtube.com/watch?v=Rrpk-fTG5Dw) (video)
   * If you are curious about the math behind linear regression (slow): [Khan Academy - least squares fit](https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap#least-squares-regression)
   
## Week 10
 * Lab - Nov 6
   * [Slides](lectures/10_week_lab.ipynb)
   * Exercise: [exercises/glass_identification.ipynb](exercises/glass_identification.ipynb) and [exercises/glass.csv](exercises/glass.csv)
   
