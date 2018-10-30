const List= (props) => {
  { /* change code below this line */ }
  return <p>{props.tasks.join(', ')}</p>
  { /* change code above this line */ }
};

class ToDo extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>To Do Lists</h1>
        <h2>Today</h2>
        { /* change code below this line */ }
        <List tasks={['learn react', 'go to Amazon Go store']}/>
        <h2>Tomorrow</h2>
        <List tasks={['catch up with classes', 'do HackerRank challenges', 'work on SPD projects']}/>
        { /* change code above this line */ }
      </div>
    );
  }
};