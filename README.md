
<p align="center">
   <img src="https://lh3.googleusercontent.com/pjuqWGUogguB1YtD3mujtbKJjfriMyPOhskCnF_7G0g4zFmisO8Er6uzFwJziKSvwsKbAu7e3n4bIE8az2i-a1rrP8vRUhszRNqZXEWTLe5KEheukBUVF7ktDDXYkvHz07mQAnD4k9O7u50SJkRbQYcu7ulKw04ieW9ec3l0Td8v1OZj7g_qDjz0_kfCspUsl3CQXapjTjOge0N1p4gJX1yaUzlGEr7IhfIXZdllX0dUj1OU2ry9K5JEDZw_27EATGbOXDh20oENKUps1TmVylAM5QIMc1fhqqEca7KBwInmYbAEOPSTxvwP7BnWixH6KQ3NcbkS-8MyyoDqrZZkA1Yp4Io6OjzGidkIVijTg-9sb8IV51HNqMKkaklZBWDwg5KrGycsPS5_EkQh9JLhKpnCWzbYloRHuOgKWZE4OLJ4MUi1E7KFMnKHkfZOSrwk-LLUKsaI4c_XNQIiK9lPQRHFtWYl7EYIVvkYFsoZ9lYrGTTr2p-Sn2v0bFR7HatuD4F49o3ceUllxfjR2LvE4VK0m6nZU1SfC4Fi3hBHyPkv62wmZQturOeBPhVha9BRFxDxFhfNgiphS8cepHgOx1ZQcobYXj68MegQrU16GmDT9pkamyiQggKWWfS2ZpPP2yCn2ybrEX1iiYi62NS05p81H6cfqh-iM4MiMLl2WEscI93q8BA1gc7NIJJ_b1s=w512-h338-no" alt="Strivio Logo"/>
</p>

## Usage

## Organizers

 1. Head to [DropBox](https://www.dropbox.com/developers/apps_tk=pilot_lp&_ad=topbar4&_camp=myapps) and Create an App
 2. After you Create your Dropbox App click on Generate Access token and Copy it.![enter image description here](https://miro.medium.com/max/938/1*vLvuPuX5n-klKMConAXQug.png)
3. Create a File Known as 🗃️ "IO.yaml" for all the Input / Output Test Cases
4. The File should Look like this
```yaml  
inputs:  
  input1:  
    1  
  input2:  
    2  
  input3:  
    3  
  input4:  
    4  
  input5:  
    5  
outputs:  
  output1:  
    2  
  output2:  
    3  
  output3:  
    4  
  output4:  
    5  
  output5:  
    6  
```
5. Upload this to the **Root Directory** of Drop Box and done 😃!
6. Send the OATH token to participants - this works like an access token for the workshop.
## Participants
1. In GitHub Repo open Settings/Secrets and create a Secret
2. Name of the secret should be **OATH** and value should be **OAUTH_ACCESS_TOKEN=** the access token which the organizer gave you!

Example: 

![enter image description here](https://lh3.googleusercontent.com/FWyw9eCgKusbUT7w6jKiITafU7ZNp3el4QiwyTM1evxo8J181AvS3QZjDsNfzs4Rkgo8Uoz91_BOK06ci8zusVtdFHbPZ1nl_I6xCeIxHXJql10kLY5IOu7mxSF9mflOTd6gp1xpxfBsyf8n9kf66UWKiV8HDMrcyU051mj7RfG3PM5EPeIoWlcy9Zkp2-pNkZ2vQkjvq5LN195LNbkeRifOVmphYaBESLMnV9oUlPyMQB-mBouELuh_XSKWAe3ZYwksV4pLpkAgIDeTL6HcOXLslcCtSaon3PHHTUS3SmteC1IpPLHOtw1NHbH8iH4skLGS-7wGVloA7Tw3Yuplxw2iKTnilWFQ-jZY1vAXLRaV-rCZ-R5sKHzt3evspTpmaNvhojN2v-mXqEQvR2Av_nr3YfhxwAz8JLi1kvOvJ0IgfT9MUYuMPKBQ-y6I8BlhkiZBUrCd4xHkc5JOcGyqA-u8i2lPrnPrOqPEzAggC1J7P5dg8btsrnkvKwB5y1Hc9A4-pKMsVayDyXReGrAwzIAld-Jril-cyaUI6BDdAFSLqKVuYhjPRvizEtHgYbnUAEjD899FCUPLcn4ZCyJwGu2q4EN4WJPkndwYkEF105CwKMP77ekK-DbdZZl3ne6eeVbDaps0SbG9MBOM6YaIyTJ_cna-M41uUIVrd0uLcksFe2q1pVKuMZTJ0f7CYU014QRc7NUn348J5pq_tSg1NmEL3vlyp9iYnXt6wynAsvCVuKBQGLjHyAKN=w931-h753-no)

![enter image description here](https://lh3.googleusercontent.com/AhSH9lwyBRJuEuODKSrr-K-ap-EoRviAS3oA_WwEh5Cz33dAmSIoQujt-YfCvMZXvxAM1PFr-xGmPg86mMfQPraXv2rsr8FP-u7Bp84x513Q-DhaSVVW1W2mcX3hkt-udc4-tQN7Beb3JMUyG-rAVmMLSn0boetZ_g3FnXBXaLsdzktrhHEpwNpGzu9AMETT1eEs4dG1Pmec5FQpKcDegSi5EMhLlWN8xCbEh5H-loaqqvxan-ow0Mctx-gTyPGKEi-6qprKEH3AOKhmd-z4uXAfjhcxr7rXs92dPlxXBkBQlel0qMPimLikyR6Hkgp4TL58mhqdGMUAbDJ391kq7KXZk67rTvyvASukKaGSMJ5kC2yMwBDmD_RUJLHTDnBQ30cUGPZ2ZVJgBhlNCLZkwxIw_ik_GM-nbLyTG9yF7VGCSxPHQGIiL1KW2Cj1LIbyNWR9G5YdmXp_UNnSrScq3AQBH2wjNH1gMWQv4TyB9kAbDI_QrWNsFZHk6HgbBzprlJNikIaGMf39YGkJH81gt7XKLcxuoazbEFdpqQTa23DWC6HX6aRm8zjddudREt7J5GMnbRuterdrAPYeazf7rXfi6Z0Yh3aWGwYzFkimLasvJbtRmd4jP79a3urcK2ikGE-hQqMeYIS7vrUybncBpN8tlURXH5nAgRHTHXkebm3BXA1SvGKLS7z-HQwmKLbduM020F1pQud6CoZ1D1SVeT-Bboc6igNWzM-o0ICcOjTaZl5g=w975-h386-no)
3. Click on actions
![enter image description here](https://lh3.googleusercontent.com/GbdrYDNw6P_my4YNcLwXFZSWJp-4inNUe71SR8vOYceeepla2Ez8PPUFcFn89dSswVzamiUs4eNwN7Hop5ShC0FD-kkf9HkMuMt2OQtkWotw8kcxjn0CE87Nu7IA_l4FCNz-XETQrWma_Sa4M7eN1N7QQ0wIse4oBrjjwNhHu8PDwQjV-FTNbhzytlItTAhzfIXektBiP3YGKyvBsXT4IOL_tkp1jpzG1H5JO5dZYAytsEqOIAlrATPONrUTDlIHb_Fp2qb4OOBYXmpIbioCSlRSAQlg4pC_QMzwbdlC-wP24tmYnKJTQpxmdXIs4_5ObcooCKbRuwXkaMP61uSilxv1YLRQb_-UDZ5Swgox2qKCuLmr6Sb1bVjuQFa4YAlydDi8EJxZAocPFRhJRomz9Jph28GingfEz_l9MlxBEoySPOb2E94Z8l6apM2yk9gvOg1FZY9Dof8U57WA28zroD_FuHypiuGk5qGg5bPgsTwf66KB24pbhPuXrUti4wpT5_wsK5qJzbqBI6MLKjgW2us0QBSoJilF7lo4J26vSQeJ2qLzwJHXqYejn4KqfGFKg2Wm2Pmim_NFeheTHDBa3VZvGprBBzRmvE7gAcSKJoinZYRrFtq3IkTYRYPQ_BZsoKtk6WJwAoSNXvXoD4UseK5fPZ6WHRKvBexJpyPM7HHtSxpNg4CUvCApODLCan3oOrpdHXcY32wnzh9sZMQhi8AnxFnQpVKhQHiDNqytYusML9_p=w1203-h87-no)
4. Click on Set up a workflow yourself
![enter image description here](https://lh3.googleusercontent.com/BfdHTR0sxaUJbgsvEfcHCKoFzpOlW43f9fMMubIlw8C42NpAORuV9NAFlpjny0c3fmG2Gh3SHZrR2Gd14D0dJObPFNXwVXtThEO2ZGRVfEbR4s76KVI20KJIV3HfMhaYwdg_u9C6Ic4=w1860-h243-no)
5. Delete everything and paste the below code
```yaml
name: Evaluation
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run action
      uses: jainal09/strivio@master 
      with:
        oath: ${{ secrets.oath }}
```
Click on `start-commit`

6. Now its time to start coding!  Clone your repo and start working on the problem.

7. Supported Programming Languages `python, java, c++, c`

8. Create a file program.***extension*** - supported extension`.c .cpp .java .py`

NOTE: for java Class name should be Main

9. After Coding is done create a file 🗃️ **"lang.yaml"**

10.  Add the below code.
```yaml
language:
  python3
``` 

11. Replace the name of Programming Language in the above code as follows.

` python - write python3`
`java - write java`
`c++ - write cpp`
`c - write c`

***No language other than above are supported!***

12. Commit the code and push

13. Head to GitHub and select Actions
![enter image description here](https://lh3.googleusercontent.com/GbdrYDNw6P_my4YNcLwXFZSWJp-4inNUe71SR8vOYceeepla2Ez8PPUFcFn89dSswVzamiUs4eNwN7Hop5ShC0FD-kkf9HkMuMt2OQtkWotw8kcxjn0CE87Nu7IA_l4FCNz-XETQrWma_Sa4M7eN1N7QQ0wIse4oBrjjwNhHu8PDwQjV-FTNbhzytlItTAhzfIXektBiP3YGKyvBsXT4IOL_tkp1jpzG1H5JO5dZYAytsEqOIAlrATPONrUTDlIHb_Fp2qb4OOBYXmpIbioCSlRSAQlg4pC_QMzwbdlC-wP24tmYnKJTQpxmdXIs4_5ObcooCKbRuwXkaMP61uSilxv1YLRQb_-UDZ5Swgox2qKCuLmr6Sb1bVjuQFa4YAlydDi8EJxZAocPFRhJRomz9Jph28GingfEz_l9MlxBEoySPOb2E94Z8l6apM2yk9gvOg1FZY9Dof8U57WA28zroD_FuHypiuGk5qGg5bPgsTwf66KB24pbhPuXrUti4wpT5_wsK5qJzbqBI6MLKjgW2us0QBSoJilF7lo4J26vSQeJ2qLzwJHXqYejn4KqfGFKg2Wm2Pmim_NFeheTHDBa3VZvGprBBzRmvE7gAcSKJoinZYRrFtq3IkTYRYPQ_BZsoKtk6WJwAoSNXvXoD4UseK5fPZ6WHRKvBexJpyPM7HHtSxpNg4CUvCApODLCan3oOrpdHXcY32wnzh9sZMQhi8AnxFnQpVKhQHiDNqytYusML9_p=w1203-h87-no)
14. Select your last commit, click build and click Results 🤞
![enter image description here](https://lh3.googleusercontent.com/wwYJR6AaxTNMK1BVWNNZaKEfc5XQwpAXZSqedtnVZu7WFO7pYdGnvpBngqOcRJOuLnaWeo9liBU6jFoLu6W1jKYhSeJyyNL4pqSIB6JnT0gA_-gD6hQC00wbwW4HebwC5MCrFDa6HM5CKA7wQ-JD_ScNyKIPU9cKQfx43UMCHDauAHd3aPvMmFBuHpqjbcKAZly_YZ49Goor3bNArTJTtkDy2ATE2WTNJjmQjwS4pFALXCRQg_HAQcKWZaBU7HcHubxrA21aiSUSH-1ZWSIUOL1QKEVsFrDjpHBZdOC5Uan6Y0VYrejnXVwTsJUzc0PxbK2uuYYV4Y-hTwhq3-TMCNfNVBdhz-myHkSmMIoM4orDa-7r9A_iNBzHTVMfmWp2UhRVISL7n2iGjkGAA_QfeEjaw3HrSEDAACt0xXEUhIjWVQ_KrkIUpJlArjRDVWqlkT_yWZL1phs6_HA7K8XaHyF2ovoRZtka7YZq8hVy1-Ys8qW5t2Ec0BkMNCchZ7LxvQuDZCxjQPwZlYjRTZBSZF3YsUQaWQOUS1BCPl1egd0ZQyp0hXD18VHN3pS5NkW0NjfsIrH07EU8qwX59PjPw-MLjTpkBR3LR8vQtQ7-8DYVhHbb1xyZv5fZuNBocx3FRrJAkP_57MoQWNcdn38DG493sB6JUb1AD9CO2rwAto_S79JD0d3m25qU3c4DWBRneKLg8erhW5YKY6zObZRJkBszSFNlZJ4Bd1ZYe9KUlGwHaq3w=w1440-h245-no)
15. Check if your code passed all the Test Case ✔️ or ❌

![enter image description here](https://lh3.googleusercontent.com/fcgkExGB9GfqyzwilyWSF0PTlNmx_7zxixYwtSZyZ3QUTZy-TGA56rpg92WYvhHX0BMvx-PV6rJSYILwcxslKMnUNNJcduHDyvwkY0fcEXyzEY5nN3d9Z47gAfqnkG5xmptR4rIjfn8oa2chIXiZ7hsQY7Evl9kOsIcxynJueJibi8dScoXYNtd90Rgc2Fi_oT7OhtJKjvaVlxYaR4AhTDFrsy_1VksCThDR9hAPhF3e3QWncYfO28wczHDe80YQ_x7ZAn_5yLV1SYHc23n3Xq2seaI-j5F8rBFPkjlfC7WX70I52hAybSNet7MKZG1PvIpnTSZKjU35N9SoDfnjGJv5W6rxdLY9y-_tx2zAs1qp6HaIx0XQNBpoCJeVv90p_3pS7cLVhgd-pA7upl23B5WcGHKe4bpKojav1jqRZrUu5fN9R7Ic2pA82-cgfrtVSWXt6v3_LxR0LiRaDR-xrvxmGCEQI4-a6vDZlqMfLcVF9jmamILtwtbIuPvv8hxOivoe_IjPB5lkAnP6vMSsqv4fuEagFHuy4rMiFO6bTeReM1wdvCvnssM-E9b34z-FeW5UP6WICqvSEdK_p79XdzSmx3zL3iagXweSlwcriKJSSuxr9xtdPkgdv1UwfF_yfOWAWFv4GjFCWvfCDee40O_2zZoynFYUx9RaZ9R2TemE1_G3D06DH7wNA9KOLEWtX32R2CFGHTLwZTZdjeoj9fS8qYH9SYkY2d8E8g3eSi-vlLte=w367-h125-no) 

 *Success Full Build with all Test Case Passed*
 
![enter image description here](https://lh3.googleusercontent.com/dw50RL8AZ4_qJnLj5s-yP8RjWlZ4jaxzIoBVPDmxuA_ePkh60nZNjPWR_cr-QQ8rNrOr61LHaV8cMK9MigDQV_Q-brhyjmwfrGo9__fM78O1G57FwCoJBVLol4nv_YzBH4tQi-7TaCekp9-Rn9qScK3kSnrpdYDVYXnnxtxB-iiGmLEsVX0kIaRQXTuCfClpoRXDAA3YCzltJuQl6UPvUKzUKWLhsiLJuoP5SKU35INUZuI5Kj5dI0EddEq2JuWkJtsTfBy3p3wimd5eZWx6mItgh4ev15Iy5i2M0xIy20a3PNTtPoi5uVIqFeJtHryuoCSTkwkTn6o3bCXWaOQ9dMCSdLH9Yo1-fF1cyueuSRYRRXyF-cVpwWlLuxPLhZalD9de66uI1ul2RHD3HDQlOQhX8yc0odNQj_BrqxXp9N4Fk2lI60eXODdUfzuInjM7UlYGVk4kNr1uJlNOuDD41DlarPaqvrJuSQaj8xm5M5w98r6mLheumxwbGoNwhifSxjecpYo20U_qLFTvkT5Tar_UqnBJr_m0EJMN6nyqxf-0z9MHCPAyyDTt_fnctdn966Wc12_8eCHJbb54Vd0XffVXrVibyzJd7MPHs_viycXnQbj4sNBXAOTKet5_SBGaNiK3EZMamb9Ebm-hO5HQm2IB2vkHJEuulJ5aNMT6RFe4glhVVgai6bz1Hkn4j9FpXdcjRaYhyzz6KKCqYTGx71kpfQbvsgkm3wG3j1zMvayh1Liu=w1440-h401-no)
*Build Failed as Code Didn't Passed all the Test Cases*



**Done! thats how you can host coding competetion on GitHub like Hackerrank etc** 
