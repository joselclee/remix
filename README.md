# remix
Application that uses Spotify's API and a content-filtering based recommender system to recommend new songs that might appeal to the user. 
### Planned Features:
<ul>
  <li>Spotify Login and playlist(s) linking.</li>
  <li>Suggest "same-vibe" songs based on Spotify account or playlist(s) provided.</li>
  <li>Suggest songs based on selected "mood".</li>
  <li>Suggest similar songs based on one song provided</li>
</ul>
<br>
When suggesting songs, a list of 10 songs maximum will be displayed on the screen with the option of playing it.
<br><br>
Below is a short description of how each feature is achieved.
<ul>
  <li>Same-vibe recommendations is achieved by using Spotify's recommender endpoint with a score calculated by the recommender system via the inputted playlist(s) or the top* 100 songs of the account provided.</li>
  <li>Mood recommendations are based on preset inputs that are sent to Spotify's recommender endpoint along with the user profile.</li>
  <li>Similar songs based on one song are recommended via Spotify's recommender endpoint + custom inputs from the model to tighten results.</li>
</ul>
<sub>*top songs are based on yearly stats not all-time.</sub>
<sub>Model training is done with last.fm dataset NOT Spotify data.</sub>

### Currently not being deployed 5/23/2024
