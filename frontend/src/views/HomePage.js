// different pages of your application.. home page view
import React from 'react';
import Header from '../components/Header';

function HomePage(){
    return (
        <div>
            <Header />
            <p>Welcome to the EcoTracker. Here you can track and analyze environmental data.</p>
        </div>
    );
}

export default HomePage;