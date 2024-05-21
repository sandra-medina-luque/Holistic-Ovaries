import { useState } from 'react'
import './App.css'
import Recipe from './components/recipe/Recipe';
import FormContact from './components/formContact/FormContact';
import AdminPerson from './components/adminPerson/AdminPerson';
import AddPerson from './components/adminPerson/AddPerson';
import Question from './components/question/Question';
import QuestionContact from './views/QuestionContact';
import QaAdmin from './components/qaadmin/QaAdmin';
import Calendar from './components/calendary/calendary';
import Article from './components/article/Article';

function App() {


  return (
    <>
      {/* <Recipe/> */}
      {/* <FormContact/> */}
       {/*<AdminPerson/>*/} 
      {/* <Question/> */}
      {/*<QuestionContact/>*/}
      {/*<QaAdmin/>*/} 
     {/*<Calendar/> */}
      <Article/>

    </>
  )
}

export default App;
