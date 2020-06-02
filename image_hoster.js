const express = require('express');
const app = express()
const port = 5000
app.get('/:image', (req, res) => res.sendFile(`assets/${req.params.image}.png`, { root: __dirname }))
app.listen(process.env.PORT || port, () => console.log(`listening on port ${port}`))
