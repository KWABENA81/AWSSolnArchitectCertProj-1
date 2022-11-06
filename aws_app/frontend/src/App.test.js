import { render, screen } from '@testing-library/react';
import App from './App';

class App extends Component {
  render(){
    return (
      <div className="App">
        <header className="App-header">
          <h1>List of topics to show</h1>
          <h1>Ask any question</h1>
          <input></input>
          <br/>
          <h1>Answer</h1>
        </header>
      </div>
    );
  }
}

export default App;