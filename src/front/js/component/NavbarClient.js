import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Navbar, Nav, Container, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import RoadBrosLogoPhoneView from "../../img/RoadBrosLogoPhoneView.png";

export const NavbarClient = () => {
	const { store } = useContext(Context);

	return (
		<Navbar bg="dark" variant="dark" expand="lg" fixed="top">
			<Container className="md-mx-5 sm-mx-2 my-0">
				<Navbar.Brand className="fs-4">
					<Link to="/" className="name text-decoration-none text-white">
						<img alt="" src={RoadBrosLogoPhoneView} width="50" className="d-inline-block align-center" />
						<h3 className="align-center p-0 m-0">RoadBros</h3>
					</Link>
				</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" className="border-0 d-inline-block" />
				<Navbar.Collapse id="basic-navbar-nav">
					<Nav className="m-auto position-absolute bg-dark top-25 end-0" style={{ zIndex: "100" }}>
						<Link to="/ClientHomePage">
							<Button className="btn btn-outline-warning border-0 bg-transparent">Home</Button>
						</Link>
						<Link to="/ServiceMenu">
							<Button className="btn btn-outline-warning border-0 bg-transparent">Request Help</Button>
						</Link>
						<Link to="/VehiclesList">
							<Button className="btn btn-outline-warning border-0 bg-transparent">Vehicle List</Button>
						</Link>
						<Link to="/ClientProfile">
							<Button className="btn btn-outline-warning border-0 bg-transparent">Profile</Button>
						</Link>
						<Link to="/ClientContactUs">
							<Button className="btn btn-outline-warning border-0 bg-transparent">Contact Us</Button>
						</Link>
						<Link to="/">
							<Button className="btn btn-outline-warning border-0 bg-transparent">Log Out</Button>
						</Link>
					</Nav>
				</Navbar.Collapse>
			</Container>
		</Navbar>
	);
};
