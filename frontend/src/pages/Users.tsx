import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

function Users() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch(`${API_URL}/users`)
            .then(response => response.json())
            .then(setData)
            .catch(console.error);
    }, []);

    return (
        <pre>{data ? JSON.stringify(data, null, 2) : "Loading..."}</pre>
    );
}

export default Users;
