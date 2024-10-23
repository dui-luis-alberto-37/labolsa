# labolsa
## By Dr Victor De la Luz <vdelaluz@enesmorelia.unam.mx>

Market model using Montecarlo.

##License 
[GNU/GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html#license-text)

## Preview
![labolsa results](https://raw.githubusercontent.com/itztli/labolsa/refs/heads/main/stock.png)

![labolsa results](https://raw.githubusercontent.com/itztli/labolsa/refs/heads/main/stock2.png)

### Running
```console
make
./labolsa BMV 10 100 200000 > test1.dat
./visualizacion.py
```
### C requirements
*gcc
*GNUmakefile

### Python requirements
*pandas
*mplfinance
*numpy
*datetime
*re