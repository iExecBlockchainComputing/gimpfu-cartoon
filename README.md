# gimpfu-cartoon

# Off-chain gimp execution

<p align="center">
<img src="https://user-images.githubusercontent.com/6378201/129872792-fb335c10-8e2f-44fd-89e3-0004f5182308.jpg" alt="before"/>
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/6378201/129872894-ac1359d6-042e-43f1-ba99-9326eaef700a.jpg" alt="after"/>
</p>

This application leverages gimp's batch mode in order to apply a custom-made effect on a given image. The computational processing can be negociated with iExec workers. The original photo credits go to Aleksandar Pasaric.


### Running locally
>   :warning: For more visually appealing results, use high quality images with a few different colors.

Create your input and output folders, then pass them as a parameters in your docker run :

```
docker build . --tag gimpfu-cartoon
docker run --rm -v /home/user/iexec_in:/iexec_in -v /home/user/iexec_out:/iexec_out -e IEXEC_IN=/iexec_in -e IEXEC_OUT=/iexec_out gimpfu-cartoon
```
The application will process all .png and .jpg images found in $IEXEC_IN

The results can be found in $IEXEC_OUT

### Running with iExec

This section assumes you have:
 - Configured your wallet
 - Configured your API keys and chain configuration files (chain.json, iexec.json)
 - Deployed your docker image to Docker Hub
 - Deployed your application to iExec

Please refer to the [quickstart guide](https://docs.iex.ec/for-developers/quick-start-for-developers) to perform the necessary steps.

Executing in the viviani sidehcain testnet :
```
iexec app run --watch --input-files <image url 1>,<image url 2> --chain viviani --workerpool <address>
```
Additional running options can be found [here](https://github.com/iExecBlockchainComputing/iexec-sdk).

You'll find below a minimalist version of the configuration files :

##### chain.json
```
{
  "default": "viviani",
  "chains": {
    "viviani": {
      "id": "133"
    }
  },
  "providers": {
    "infura": {
      "projectId": "<infura_projet_id>",
      "projectSecret": "<infura_projet_secret>"
    },
    "quorum": 1
  }
}
```
#####  iexec.json
```
{
  "app": {
    "owner": "<your_ethereum_wallet_address>",
    "name": "gimpfu-cartoon",
    "type": "DOCKER",
    "multiaddr": "registry.hub.docker.com/<docker_username>/<docker_image_name>:<docker_image_version>",
    "checksum": "<docker_image_checksum>",
    "mrenclave": ""
  }
}
```
##### Fetching results

```
iexec task show <task_id> --download my-app-result --chain viviani && unzip my-app-result.zip -d my-app-result
```
You can also download your results using the [iExec explorer](https://explorer.iex.ec).
