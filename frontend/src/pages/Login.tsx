import Header from "../components/Header.tsx";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import crypto from "crypto-js";

const API_URL = import.meta.env.VITE_API_URL;

function Login() {
    const [login, setLogin] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const navigate = useNavigate(); // Hook for redirection

    const handleLogin = async () => {
        const hashedPassword = crypto.SHA256(password).toString();

        try {
            const response = await fetch(`${API_URL}/connect`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({login: login, password: hashedPassword }),
            });

            const data = await response.json();
            if (response.ok) {
                localStorage.setItem("token", data.token); // Line modified by AI
                localStorage.setItem("login", login);
                navigate("/");
            } else {
                setMessage(`Error: ${data.detail}`);
            }
        } catch (error) {
            setMessage("Failed to connect to server: " + API_URL);
        }
    };

    return (
        <>
            <Header />
            <h1>Login Page</h1>
            <input
                type="text"
                placeholder="Login"
                value={login}
                onChange={(e) => setLogin(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleLogin}>Login</button>
            <p>{message}</p>
        </>
    );
}

export default Login;
