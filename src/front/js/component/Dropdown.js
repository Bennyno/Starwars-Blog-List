import React from "react";
import { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import  Dropdown from "react-bootstrap/Dropdown";
import Button from "react-bootstrap/Button"

export const DropDownMenu = () => {
  const {store, actions} = useContext(Context);
  const [favorites, setFavorites] = useState({});
  const [selectedFavorites, setselectedFavorites] = useState({favorites:[]});

  const deleteFavoriteBtn = store.favorites.map((item, index) => {
    return (
      <Dropdown.Item key ={index} value={index}>
      {item}
      <Button
        onClick={()=> actions.deleteFavorites(item)}
        className = "delete">
        <i class="fas fa-trash-alt"></i>
      </Button>
     </Dropdown.Item> 
    );
  });

  return(
  <>
    <Dropdown>
      <Dropdown.Toggle variant="primary" className="dropdown-basic">
        <div className="drp">
          <div className="drp counter">
            Favorites {store.favorites.length}
          </div>
        </div>
      </Dropdown.Toggle>

      <Dropdown.Menu
        defaultValue={favorites}
        onChange={(event) => {
          setFavorites(event.target.value);
          setselectedFavorites({
            ...selectedFavorites,
            favorites: store.favorites.find(
              (item) => item.id == event.target.value
            ),
          });
        }}
      >
        {deleteFavoriteBtn}
      </Dropdown.Menu>
  </Dropdown>
        </>
    );
};