const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			people: [],
			planets: [],
			vehicles: [],
			favorites: [],
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				},
			]
		},
		actions: {
			// Use getActions to call a function within a fuction

			getPeople: () => {
				return fetch("https://swapi.dev/api/people")
				.then(response => response.json())
				.then(json => setStore({
					people:json.results
				}))
				.catch(error => console.log('error', error));
			},

			getPlanets: () => {
				return fetch("https://swapi.dev/api/planets")
				.then(response => response.json())
				.then(json => setStore({
					planets:json.results
				}))
				.catch(error => console.log('error', error));
			},

			getVehicles: () => {
				return fetch("https://swapi.dev/api/vehicles")
				.then(response => response.json())
				.then(json => setStore({
					vehicles:json.results
				}))
				.catch(error => console.log('error', error));
			},

			setFavorites: (favorite) => {
				const store = getStore();
				setStore({ favorites: [...store.favorites, favorite]});
			},

			deleteFavorites: (favorite) => {
				const store = getStore();
				const del = store.favorites.filter(item=>item != favorite);
				setStore({ favorites: del})
			},

			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMessage: async () => {
				try{
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
