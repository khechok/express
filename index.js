const express = require('express')
const path = require('path')
const logger = require('./middleware/logger')
const app = express();



//init middle ware
// app.use(logger); 
//set static folder
app.use(express.static(path.join(__dirname, 'public')))

app.use('/api/members', require('./routes/routes'))


const port = process.env.port || 1500;

app.listen(port, () => {
   console.log(`your server is runnning at port ${port}`)
})

