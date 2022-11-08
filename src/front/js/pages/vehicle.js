import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";

export const Vehicle = (props) => {
	const { store, actions } = useContext(Context);
	const params = useParams();
	const [vehicles, setvehicles] = useState();

	useEffect(()=> {
		 fetch(`https://swapi.dev/api/vehicles/${params.id}`)
				.then(response => response.json())
				.then(json => setvehicles(json))
				.catch(error => console.log('error', error));
	}, [])

	console.log(vehicles)
	return (
		<div className="jumbotron">
			<div>
			<img className = "soloimg" src="https://via.placeholder.com/300" />
			<h1 className="display-4">
				{vehicles && vehicles.name}
			</h1>
			<p className ="single"><strong>Model:</strong> {vehicles && vehicles.model}</p>
			<p className ="single"><strong>Manufacturer:</strong> {vehicles && vehicles.manufacturer}</p>
			<p className ="single"><strong>Vehicle Class:</strong> {vehicles && vehicles.vehicle_class}</p>
			</div>
			<p className="detail">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
				Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
				Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
				Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.</p>
			<hr className="my-4" />
			<Link to="/">
				<span className="btn btn-primary btn-lg" role="button">
					Back home
				</span>
			</Link>
		</div>
	);
};

Vehicle.propTypes = {
	match: PropTypes.object
};