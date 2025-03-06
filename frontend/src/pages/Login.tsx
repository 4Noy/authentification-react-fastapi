import Header from "../components/Header.tsx";

function Login() {
    return (
        <>
            <Header />
            <h1>Login Page</h1>
            {/* Available backend endpoints in this env var : VITE_API_URL=http://backend:8000
                - POST : /create_user
                    Content to send : {"login": login, "password": hashed_password}
                - POST : /connect
                    Content to send : {"login": login, "password": hashed_password}
            */}
        </>
    );
}

export default Login;
