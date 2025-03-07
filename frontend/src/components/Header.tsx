import './Header.css'
import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

function Header() {
    const isAuthenticated = async() => {
        if (localStorage.getItem("token") && localStorage.getItem("login")) {
            try {
                const response = await fetch(`${API_URL}/verify_token`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({login: localStorage.getItem("login"), token: localStorage.getItem("token")}),
                });
                return response.ok;
            } catch (error) {
                console.log(error);
                return false;
            }
        }
    }

    return (
        <>
            <header className='header'>
                <h1>Header</h1>
                <h2></h2>
                <nav>
                    <ul>
                        <li><a href="/">Home</a> </li>
                        <li><a href="/login">Login</a></li>
                        <li><a href="/register">Register</a></li>
                    </ul>
                </nav>
            </header>
        </>
    );
}

export default Header;
