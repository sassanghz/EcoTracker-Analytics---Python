import React, { useEffect, useState } from 'react';
import Header from '../components/Header';

function HomePage() {
    // State for storing the fetched data
    const [data, setData] = useState(null);
    // State for storing any error that occurs
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('/api/data')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(setData)  // Assuming data is received as JSON and can be directly stored
            .catch(error => {
                console.error('Fetching data failed:', error);
                setError(error.message);
            });
    }, []);

    return (
        <div>
            <Header />
            {error ? (
                <p>Error loading data: {error}</p>
            ) : data ? (
                <div>
                    {/* Assuming data is simple text or object that can be stringified */}
                    <p>Data: {JSON.stringify(data)}</p>
                </div>
            ) : (
                <p>Loading data...</p>
            )}
        </div>
    );
}

export default HomePage;