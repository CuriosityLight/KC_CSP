import random

chance = ""
plink1 = """    
                  o
                  .
                .   .
              .   .   .
            .   .   .   .
          .   .   .   .   .
        .   .   .   .   .   .
      .   .   .   .   .   .   .
    .   .   .   .   .   .   .   .
 |_| |_| |_| |_| |_| |_| |_| |_| |_|"""





def plinko(fun_again, plink1):
    fun_again = input("drop a ball: ")
    if fun_again == "yes":
        print(plink1)
    chance = random.randint(1, 2)
