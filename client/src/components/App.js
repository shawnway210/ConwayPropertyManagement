import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Properties from './Properties'
import NewPropertyForm from './NewPropertyForm'
import Images from './Images'
import NewImage from './NewImage'
import Reviews from './Reviews'
import NewReviewForm from './NewReviewForm'

function App() {
  const [properties, setProperties] = useState([])
  const [reviews, setReviews] = useState([])
  const [images, setImages] = useState([])

  useEffect(() => {
    fetch('/properties')
    .then((res) => res.json())
    .then((data) => setProperties(data))
  }, [])

  useEffect(() => {
    fetch('/reviews')
    .then((res) => res.json())
    .then((data) => setReviews(data))
  }, [])

  useEffect(() => {
    fetch('/images')
    .then((res) => res.json())
    .then((data) => setImages(data))
  }, [])
  

  
  return (
  <>
  <div className = "siteTitle">
  <header>
    <h1>Conway Property Management</h1>
  </header>
  </div>
      <Switch>
        <Route exact path = '/properties'>
          <Properties properties = {properties}/>
        </Route>
        <Route exact path = '/newproperty'>
          <NewPropertyForm setProperties = {setProperties}/>
        </Route>
        <Route exact path = '/reviews'>
          <Reviews reviews = {reviews}/>
        </Route>
        <Route exact path = '/newreview'>
          <NewReviewForm setReviews = {setReviews}/>
        </Route>
        <Route exact path = '/images'>
          <Images images = {images}/>
        </Route>
        <Route exact path = '/newimage'>
          <NewImage setImages = {setImages}/>
        </Route>
      </Switch>
  </>
  );
}

export default App;
