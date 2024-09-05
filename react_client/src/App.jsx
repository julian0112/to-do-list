import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { TagsPage } from './pages/TagsPage'
import { TaskFormPage } from './pages/TagsFormPage'
import { ListPage } from './pages/ListPage'
import { Navigation } from './components/Navigation'

function App() {
    return (
        <BrowserRouter>
            <Navigation />
            <Routes>
                <Route path='/' element={<ListPage />} />
                <Route path='/tasks' element={<TagsPage />} />
                <Route path='/tasks-create' element={<TaskFormPage />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App