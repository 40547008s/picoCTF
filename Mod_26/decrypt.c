#include<stdio.h>

int main(){
	char alpha[26] = "abcdefghijklmnopqrstuvwxyz";
	char Alpha[26] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char cypher[100] = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}\0";
	char plaintext[100];
	int i = 0;
	while(i < 100 &&  cypher[i] != '\0'){
		if(cypher[i] <= 'z' && cypher[i] >= 'a'){
			int pt = (cypher[i] - 'a' + 13) % 26;
			plaintext[i] = alpha[pt];
		}
		else if(cypher[i] <= 'Z' && cypher[i] >= 'A'){
			int pt = (cypher[i] - 'A' + 13) % 26;
			plaintext[i] = Alpha[pt];
		}
		else{
			plaintext[i] = cypher[i];
		}
		i+=1;
	}
	plaintext[i] = '\0';
	puts(plaintext);
	return 0;
}

