import './Header.css'
import { useState, useEffect } from "react";

const API_URL = import.meta.env.VITE_API_URL;

function Header() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [login, setLogin] = useState("");

    useEffect(() => {
        const checkAuth = async () => {
            const storedLogin = localStorage.getItem("login");
            const token = localStorage.getItem("token");

            if (storedLogin && token) {
                try {
                    const response = await fetch(`${API_URL}/verify_token`, {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ login: storedLogin, token }),
                    });

                    if (response.ok) {
                        setIsLoggedIn(true);
                        setLogin(storedLogin);
                    }
                } catch (error) {
                    console.error(error);
                }
            }
        };

        checkAuth();
    }, []);

    return (
        <header className='header'>
            <h1>Header</h1>
            <p>{isLoggedIn ? `Connected as ${login}` : "Not Connected"}</p>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/login">Login</a></li>
                    <li><a href="/register">Register</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
