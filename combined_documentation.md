# Skupper command reference

## Reference for `skupper debug dump`

Skupper allows you create a file containing all debug information.

This command includes an option to specify the platform, for example `-- platform podman` when using a Podman site.

## Reference for `skupper completion`



Output shell completion code for bash.
The shell code must be evaluated to provide interactive
completion of skupper commands.  This can be done by sourcing it from
the .bash_profile. i.e.: $ source <(skupper completion)


```
skupper completion [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

- `--kubeconfig`: Path to the kubeconfig file to use (Automatically added)

- `--platform`: The platform type to use [kubernetes, podman] (Automatically added)

## Reference for `skupper debug events`


Show events

```
skupper debug events [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper debug`


Debug skupper installation


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper debug policies`


List active SkupperClusterPolicies

```
skupper debug policies [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper debug service`


Check the internal state of a skupper exposed service

```
skupper debug service <service-name> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper delete`


delete will delete any skupper related objects from the namespace

```
skupper delete [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper expose`


Expose a set of pods through a Skupper address

```
skupper expose [deployment <name>|pods <selector>|statefulset <statefulsetname>|service <name>|deploymentconfig <name>] [flags]
```


### Options

- `--address`: The Skupper address to expose

- `--aggregate`: The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.

- `--headless`: through a headless service (valid only for a statefulset target)

- `--port`: The ports to expose on

- `--protocol`: The protocol to proxy (tcp, http, or http2) (default "tcp")

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway bind`


Bind a process to the service network

```
skupper gateway bind <address> <host> <port...> [flags]
```


### Options

- `--aggregate`: The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway delete`


Stop the gateway instance and remove the definition

```
skupper gateway delete [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway export-config`


Export the configuration for a gateway definition

```
skupper gateway export-config <export-gateway-name> <output-path> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway expose`


Expose a process to the service network (ensure gateway and cluster service)

```
skupper gateway expose <address> <host> <port...> [flags]
```


### Options

- `--aggregate`: The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.

- `--protocol`: The protocol to gateway (tcp, http or http2). (default "tcp")

- `--type`: The gateway type one of: 'service', 'docker', 'podman' (default "service")

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway forward`


Forward an address to the service network

```
skupper gateway forward <address> <port...> [flags]
```


### Options

- `--aggregate`: The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.

- `--loopback`: from loopback only

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway generate-bundle`


Generate an installation bundle using a gateway config file

```
skupper gateway generate-bundle <config-file> <output-path> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway init`


Initialize a gateway to the service network

```
skupper gateway init [flags]
```


### Options

- `--config`: The gateway config file to use for initialization

- `--type`: The gateway type one of: 'service', 'docker', 'podman' (default "service")

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway`


Manage skupper gateway definitions


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway status`


Report the status of the gateway(s) for the current skupper site

```
skupper gateway status <gateway-name> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway unbind`


Unbind a process from the service network

```
skupper gateway unbind <address> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway unexpose`


Unexpose a process previously exposed to the service network

```
skupper gateway unexpose <address> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper gateway unforward`


Stop forwarding an address to the service network

```
skupper gateway unforward <address> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper init`


Setup a router and other supporting objects to provide a functional skupper
installation that can then be connected to other skupper installations

```
skupper init [flags]
```


### Options

- `--ingress`: Setup Skupper ingress to one of: [route|loadbalancer|nodeport|nginx-ingress-v1|contour-http-proxy|ingress|none]. If not specified route is used when available, otherwise loadbalancer is used.

- `--labels`: Labels to add to resources created by skupper

- `--annotations`: Annotations to add to skupper pods

- `--routers`: Number of router replicas to start

- `--timeout`: Configurable timeout for the ingress loadbalancer option. (default 2m0s)

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper link create`


Links this skupper site to the site that issued the token

```
skupper link create <input-token-file> [flags]
```


### Options

- `--cost`: Specify a cost for this link. (default 1)

- `--name`: Provide a specific name for the link (used when deleting it)

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper link delete`


Remove specified link

```
skupper link delete <name> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper link`


Manage skupper links definitions


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper link status`


Check whether a link to another Skupper site is connected

```
skupper link status [<link-name>] [flags]
```


### Options

- `--wait`: The number of seconds to wait for links to become connected

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper`





### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper network`


Show information about the sites and services included in the network.


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper network status`


Shows information about the current site, and connected sites.

```
skupper network status [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper revoke-access`


This will invalidate all previously issued tokens and require that all
links to this site be re-established with new tokens.

```
skupper revoke-access [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper service bind`


Bind a target to a service

```
skupper service bind <service-name> <target-type> <target-name> [flags]
```


### Options

- `--headless`: through a headless service (valid only for a statefulset target)

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper service create`


Create a skupper service

```
skupper service create <name> <port...> [flags]
```


### Options

- `--aggregate`: The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.

- `--protocol`: The mapping in use for this service address (tcp, http, http2) (default "tcp")

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper service delete`


Delete a skupper service

```
skupper service delete <name> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper service label`


Manage service labels

```
skupper service label <service> [labels...] [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper service`


Manage skupper service definitions


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper service status`


List services exposed over the service network

```
skupper service status [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper service unbind`


Unbind a target from a service

```
skupper service unbind <service-name> <target-type> <target-name> [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper status`


Report the status of the current Skupper site

```
skupper status [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper token create`


Create a token.  The 'link create' command uses the token to establish a link from a remote Skupper site.

```
skupper token create <output-token-file> [flags]
```


### Options

- `--expiry`: Expiration time for claim (only valid if --token-type=claim) (default 15m0s)

- `--name`: Provide a specific identity as which connecting skupper installation will be authenticated (default "skupper")

- `--uses`: Number of uses for which claim will be valid (only valid if --token-type=claim) (default 1)

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper token`


Manage skupper tokens


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper unexpose`


Unexpose a set of pods previously exposed through a Skupper address

```
skupper unexpose [deployment <name>|pods <selector>|statefulset <statefulsetname>|service <name>|deploymentconfig <name>] [flags]
```


### Options

- `--address`: Skupper address the target was exposed as

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper update`


Update the skupper site to 1.5.3

```
skupper update [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper version manifest`


Report the version of the Skupper images by default and the value of the environment variables

```
skupper version manifest [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]

## Reference for `skupper version`


Report the version of the Skupper CLI and services

```
skupper version [flags]
```


### Options

- `--kubeconfig`: Path to the kubeconfig file to use

- `--platform`: The platform type to use [kubernetes, podman]
