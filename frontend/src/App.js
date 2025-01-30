import React from 'react';
import { Route, Switch } from 'react-router-dom';
import HomePage from './views/HomePage';
import AboutPage from './views/AboutPage'; // Make sure to create this component

function App() {
  return (
    <div className="App">
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/" component={AboutPage} />
      </Switch>
    </div>
  );
}

export default App;
