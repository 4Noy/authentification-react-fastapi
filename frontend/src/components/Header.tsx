import './Header.css'

function Header() {
    return (
        <>
            <header className='header'>
                <h1>Header</h1>
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
