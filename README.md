# labolsa

**By Victor De la Luz** :mexico:

<vdelaluz@enesmorelia.unam.mx> 

Market model using Monte Carlo simulation. In this version, we implement uniform random distribution probabilities to represent the risk associated with each user in the market. The model incorporates the law of supply and demand, along with rules for maximizing gains and minimizing losses. The initial distribution of capital is equal for all users, and stocks in the market are fully allocated during the Initial Public Offering (IPO) at the beginning of the simulation.

## License 
The code is licensed under [GNU/GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html#license-text).

## Preview
![labolsa results](https://raw.githubusercontent.com/itztli/labolsa/refs/heads/main/stock.png)

![labolsa results](https://raw.githubusercontent.com/itztli/labolsa/refs/heads/main/stock2.png)

### Running
```console
labolsa <code> <users> <stocks> <orders>
```
where:
* Code: A string with a maximum length of 8 characters representing a generic name for a set of stocks.
* Users: The total number of participants in the market.
* Stocks: The number of different company stocks available in the market.
* Orders: The maximum number of open orders allowed at each step of the simulation.


> [!IMPORTANT]
> For this version, the amount of money, the number of shares for each stock, and the initial price are fixed within the code.

### Example
```console
make
./labolsa BMV 10 100 200000 > test1.dat
./visualizacion.py
```
### Output
```console
#Labolsa simulator ver 20241022_1902
# GNU/GPL License
# By: Victor De la Luz <vdelaluz@enesmorelia.unam.mx>
#Generating 10 stock... #Ready!
#Generating 100 users... #Ready!
#Memory used: 1.855440 Mb 
#Computing IOPs...
#IOPs iterations: 3
#Running Montecarlo...
#0:#Creating NEW orders (old 0/0):
#Order created!#Buy Orders:283	Sell Orders:76.
#Executing orders...
#Executions:73
#CODE	MIN		BEGIN		AVERAGE		END		MAX
MEX0	10.095710	10.095710	10.103587	10.119341	10.119341
MEX1	9.858932	9.892323	9.976418	9.936522	10.139204
MEX2	9.971472	10.050934	10.058569	10.151121	10.173746
MEX3	9.992453	10.099042	10.089168	10.180940	10.180940
MEX4	10.000000	10.000000	10.000000	10.000000	10.000000
MEX5	9.966630	10.091102	10.087646	10.160240	10.179475
MEX6	10.073426	10.077458	10.105663	10.135885	10.135885
MEX7	9.958004	9.958004	10.054757	10.106462	10.183535
MEX8	9.843668	9.933672	9.968745	10.129037	10.129037
MEX9	10.013399	10.013399	10.129775	10.173284	10.199400
#1:#Creating NEW orders (old 238/48):
#Order created!#Buy Orders:179	Sell Orders:120.
#Executing orders...
#Executions:251
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

### Testing
The code was tested (passed) by lost of stock, tracing of excuted orders, and amount of money for each player.

