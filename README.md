# greenturtle 

api for tensorflow model hosted on heroku 

<sup>sauce: https://medium.com/@limkenghin/deploying-tensorflow-2-0-model-on-heroku-1b5cd49f8a2</sup>


<br>

### re: colossal slug size 

`tensorflow-cpu` in `requirements.txt` so the slug size is *actually* under 500mb  
<sup>(as opposed to just `tensorflow`)</sup>

<sup>sauce: [stack overflow](https://stackoverflow.com/questions/61062303/deploy-python-app-to-heroku-slug-size-too-large)</sup>


### re: app crashing because it exceeded the memory quota 🤠

<sup>when you're getting `R14` and `R15` (especially `R15`'s) and stuff is crashing and burning</sup>

use 2 workers.

just reduce the number of workers. 

<sub>sauce: [heroku](https://devcenter.heroku.com/articles/ruby-memory-use#too-many-workers) </sub>


### re: cors issues galore 

<sup>all my homies hate cors issues</sup>


##### re: flask_cors 

<sup>sauce: [stack overflow](https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask)</sup>


##### re: "non-simple" requests

`Access-Control-Allow-Methods`,, *shakes fist*

<sup>sauce: [stack overflow](https://stackoverflow.com/questions/10636611/how-does-access-control-allow-origin-header-work)</sup>




