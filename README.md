# labolsa

**By Victor De la Luz <vdelaluz@enesmorelia.unam.mx>** :mexico:

Market model using Montecarlo. In this version we implement uniform random distribution probabilities for risk of each user in the market. We implements the offer-demand law and the maximum-winning and less-lost laws. The distribution of money is the same for all users and the stocks in the market are fullfilled in the IOP at the begining of the model. 

## License 
The code is licensed under [GNU/GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html#license-text).

## Preview
![labolsa results](https://raw.githubusercontent.com/itztli/labolsa/refs/heads/main/stock.png)

![labolsa results](https://raw.githubusercontent.com/itztli/labolsa/refs/heads/main/stock2.png)

### Running
```console
labolsa <code> <users> <stocks> <orders>
```
where
* code: String of maximum 8 characters to generic name of set of stocks.
* users: Number of players in the market.
* stocks: Number of different company stocks in the market.
* orders: Maximum number of open orders for each step in the simulation.

> [!IMPORTANT]
> The amount of money, number of actions by stocks, and begin price is fixed into the code.

### Example
```console
make
./labolsa BMV 10 100 200000 > test1.dat
./visualizacion.py
```
### C requirements
* gcc
* GNUmakefile

### Python requirements
* pandas
* mplfinance
* numpy
* datetime
* re