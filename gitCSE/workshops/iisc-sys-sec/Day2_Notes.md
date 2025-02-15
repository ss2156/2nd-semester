### Data Corruption by Buffer Overflow
Suppose we have following lines of code

```
user_get_input(0)
int user_get_input(int auth_val){
char buff[1024];
        //buffer overflow area
get_input(argv);

int auth = auth_val;
if(auth){
    //authorization processed
}
else{
    //unauthorised 
}

}
```

now by using buffer overflow vunerability we can craft such that the value of auth can be changed from unauthorized to authorized.
