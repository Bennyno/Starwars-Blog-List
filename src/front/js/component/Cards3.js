import React from "react";
import { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import  Dropdown from "react-bootstrap/Dropdown";
import Button from "react-bootstrap/Button";
import { Link } from "react-router-dom";

export const Card3 = (props) => {
  const { store, actions } = useContext(Context);
  
  return (
    <>
      <div className="card-body">
      <img
        src="https://via.placeholder.com/300"
        className="card-img-top"
        alt=""
      ></img>
        <h5 className="card-title">{props.name}</h5>
        <p className="card-text"><strong>Model:</strong> {props.model}</p>
        <p className="card-text"><strong>Manufacturer:</strong> {props.manufacturer}</p>
        <p className="card-text"><strong>Vehicle Class:</strong> {props.vehicle_class}</p>
        <Link to={"/vehicle/" + (props.index + 1)} className="btn btn-primary">
          Learn More
        </Link>
        <button className="heart" onClick={()=>actions.setFavorites(props.name)}>
        <i className="far fa-heart"></i>
        </button>
      </div>
    </>
  );
};