import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import { PropTypes } from "prop-types";
import { Context } from "../store/appContext";

import "../../styles/demo.scss";

export const TruckerEditProfile = () => {
	const { store, actions } = useContext(Context);

	const [updatedUser, setUpdatedUser] = useState({
		full_name: store.loggedUser.full_name,
		email: store.loggedUser.email,
		phone: store.loggedUser.phone
	});

	const handleChange = e => setUpdatedUser({ ...updatedUser, [e.target.name]: e.target.value });

	return (
		<div className="container py-4 px-3 text-center text-light fs-4 my-3">
			<h1 className="text-center my-5">User Information</h1>

			<h2>Change your information on the fields below</h2>

			<form className="text-start">
				<div className="form-group my-1">
					<label>Full Name</label>
					<input
						type="text"
						className="form-control"
						placeholder="Edit Full Name"
						name="full_name"
						onChange={handleChange}
						value={updatedUser.full_name}
					/>
				</div>
				<div className="form-group my-1">
					<label>Email</label>
					<input
						type="email"
						className="form-control"
						placeholder="Edit email"
						name="email"
						onChange={handleChange}
						value={updatedUser.email}
					/>
				</div>
				<div className="form-group my-1">
					<label>Phone</label>
					<input
						type="text"
						className="form-control"
						placeholder="Edit Phone Number"
						name="phone"
						onChange={handleChange}
						value={updatedUser.phone}
					/>
				</div>
			</form>
			<Link to="/ClientProfile">
				<button
					className="btn btn-warning btn-lg p-2 w-75 m-auto my-3"
					onClick={() => {
						actions.updateProfile(updatedUser);
					}}>
					Save Changes
				</button>
			</Link>
		</div>
	);
};
