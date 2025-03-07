import Header from "../components/Header.tsx";
import {useState} from "react";
import {useNavigate} from "react-router-dom";
import crypto from "crypto-js";

const API_URL = import.meta.env.VITE_API_URL || window.location.origin.replace("5173", "8000");

function Register() {
    const [login, setLogin] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    const handleRegister = async () => {
        const hashedPassword = crypto.SHA256(password).toString();

        try {
            const response = await fetch(`${API_URL}/create_user`, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({login: login, password: hashedPassword}),
            });
            if (!response.ok) {
                setMessage("Couldn't create user.");
            }
            else {
                navigate("/login");
            }
        } catch (error) {
            setMessage("Failed to connect to server: " + API_URL);
        }
    };

    return (
        <>
            <Header />
            <h1>Register Page</h1>
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
            <button onClick={handleRegister}>Login</button>
            <p>{message}</p>
        </>
    );
}

export default Register;
