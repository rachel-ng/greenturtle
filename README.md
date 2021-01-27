# greenturtle 

api for tensorflow model hosted on heroku 

<sup>sauce: https://medium.com/@limkenghin/deploying-tensorflow-2-0-model-on-heroku-1b5cd49f8a2</sup>


<br>

#### re: colossal slug size 

`tensorflow-cpu` in `requirements.txt` so the slug size is *actually* under 500mb  
<sup>(as opposed to just `tensorflow`)</sup>

<sup>sauce: [stack overflow](https://stackoverflow.com/questions/61062303/deploy-python-app-to-heroku-slug-size-too-large)</sup>



#### re: app crashing because it exceeded the memory quota 🤠

use 2 workers.



