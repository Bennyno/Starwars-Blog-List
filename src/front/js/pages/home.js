import React, { useState, useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Card } from "../component/Cards";
import { Card2 } from "../component/Cards2";
import { Card3 } from "../component/Cards3";
import { Link, useParams } from "react-router-dom";

export const Home = () => {
  const { store, actions } = useContext(Context);
  
  useEffect(() => {
    actions.getPeople().then(()=> console.log(store.people));
  }, []);

  useEffect(() => {
    actions.getPlanets().then(()=> console.log(store.planets));
  }, []);

  useEffect(() => {
    actions.getVehicles().then(()=> console.log(store.vehicles));
  }, []);

  return (
    <>
    
      <h1>
        <strong>Characters</strong>
      </h1>
        <div className="card">
        {store.people.map((person, index) => {
            return (
              <Card key={index}
                name={person.name}
                gender={person.gender} 
                hair_color={person.hair_color}
                eye_color={person.eye_color}
                index = {index} />
            );
          })}
        </div>
        
      <h1>
        <strong>Planets</strong>
      </h1>
        <div className="card">
        {store.planets.map((planet, index)=>{
            return(
              <Card2 key = {index}
              name={planet.name}
              population={planet.population} 
              terrain={planet.terrain}
              gravity={planet.gravity}
              index = {index}/>
          )})}
        </div>

        <h1>
        <strong>Vehicles</strong>
      </h1>
        <div className="card">
        {store.vehicles.map((vehicle, index)=>{
            return(
              <Card3 key = {index}
              name={vehicle.name}
              model={vehicle.model} 
              manufacturer={vehicle.manufacturer}
              vehicle_class={vehicle.vehicle_class}
              index = {index}/>
          )})}
        </div>
    </>
  );
};
