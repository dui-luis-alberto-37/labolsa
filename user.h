#ifndef USER_H
#define USER_H

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */
  
#include "stock.h"
#include "common.h"
#include "market.h"
#include <string.h>
  

  User newUser(int index, float money);

  //ask to participate in buy action in stock
  int askOrderBuy(User user, Stock stock);

  //ask
  int askOrderSell(User user, Stock stock);

  int get(User user, char key[]);
  
  void insert(User *user, char key[], int value);

  void printMap(User user); 

  float value_in_stocks(Market *market, User user);
  
#ifdef __cplusplus
} /* extern "C" */
#endif /* __cplusplus */

#endif /* USER_H */
