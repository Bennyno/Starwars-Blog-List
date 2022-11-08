import React, {useState, useEffect, useContext} from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import { DropDownMenu } from "./Dropdown";


export const Navbar = () => {

  return (
    <nav className="navbar navbar-light bg-light">
        <div className="navbar-brand">
        <Link to="/">
          <img
            className="StarWarsLogo"
            src="https://i.pinimg.com/736x/b7/4b/42/b74b4283265bb86de39890cd84eb03d1--star-wars-holiday-special-website-features.jpg"
          />
        </Link>
        </div>
        <div className="dropdown">
          <DropDownMenu />
        </div>
    </nav>
  );

  
  // return (
  //   <nav className="navbar navbar-expand-lg bg-light">
  //     <div className="container-fluid">
  //       <a className="navbar-brand" href="#">
  //         <img
  //           src="https://i.pinimg.com/736x/b7/4b/42/b74b4283265bb86de39890cd84eb03d1--star-wars-holiday-special-website-features.jpg"
  //           width="90px"
  //         ></img>
  //       </a>
  //          <div className="dropdown">
  //         <button
  //           className="btn btn-primary dropdown-toggle btn-lg"
  //           type="button"
  //           data-bs-toggle="dropdown"
  //           aria-expanded="false">
  //           Favorites
  //         </button>
  //         <div className={store.favorites.length > 0? "dropdown-menu show" : "d-none"}> 
  //           <ul>
  //             {store.favorites.length > 0? store.favorites.map((favorite, index) => (
  //               <li key={index}>
  //                 <span>{favorite.name}</span>
  //                 <span onClick={() => deleteFav(favorite.name)}>delete</span>
  //               </li>
  //             )):null}
  //           </ul>
  //         </div>
  //       </div>   
  //     </div>
  //   </nav>
  // );
};
