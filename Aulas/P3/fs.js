var http = require('http')
var url = require('url')
var axios = require('axios')
var fs = require('fs')

htpp.createServer((req, res) => {
    console.log(req.method + " " + req.url);

    if(req.url == '/')
    {
        fs.readFile("web.html", (erro,dados) =>{
            res.writeHead(400, {'Content-Type': 'text/html'});
            res.write(<p>Erro: Pedido não suportado</p>);
            res.write(<pre> + req.url + </pre>);
            res.end();
        })
        res.end()
    }
    else if(req.uel == 'w3.css')
    {
        fs.readFile('w3.css', (erro, dados) => {
          
    else if (req.url == '/animais') {
        
    }axios.get("http://localhost:3000/ocorrencias")
    .then(resp => {
        
    })
    else{
        res.writeHead(400, {'Content-Type': 'text/html'});
        res.write(<p>Erro: Pedido não suportado</p>);
        res.write(<pre> + req.url + </pre>);
        res.end();

    }.listen(2702)