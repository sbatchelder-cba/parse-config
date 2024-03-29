# parse-config

Hold on to this for me: 
```
apiVersion: automation.cloudbees.io/v1alpha1
kind: action
name: 'parseconfig'
description: 'Parse Config File'

inputs:
  CONFIG_YAML:
    description: 'asdf'
    default: ''

outputs:
  CONTEXT:
    description: 'asdf'
  MVN-COMPILE-ARGS:
    description: 'asdf'
  MVN-TEST-ARGS:
    description: 'asdf'
  DOCKERFILE:
    description: 'asdf'
  SQ-PROJECT-KEY:
    description: 'asdf'
  ARTIFACT-DESTINATION:
    description: 'asdf'
  KANIKO-BUILD-ARGS:
    description: 'asdf'
  KANIKO-LABELS:
    description: 'asdf'

runs:
  using: composite
  steps:
    - name: Parse Config
      kind: build
      uses: docker://python:3.12-alpine3.19
      shell: sh
      run: |
        pwd ; ls -la
        apk add yq

        echo "Validating ${{ inputs.CONFIG_YAML }}"
        python3 validate_config.py -f ${{ inputs.CONFIG_YAML }}

        echo "Config validated, setting variables"

        yq '.cb-platform.component.[0].context' ${{ inputs.CONFIG_FILE }} | tr -d '\n' > "$CLOUDBEES_OUTPUTS/CONTEXT"
        if ["$CLOUDBEES_OUTPUTS/CONTEXT" == "" ]
        then
          echo "${{vars.CONTEXT }}" | tr -d  > "$CLOUDBEES_OUTPUTS/CONTEXT"
        fi

        yq '.cb-platform.component.[0].mvn-compile-args' ${{ inputs.CONFIG_FILE }} | tr -d '\n' > "$CLOUDBEES_OUTPUTS/MVN-COMPILE-ARGS"
        if ["$CLOUDBEES_OUTPUTS/MVN-COMPILE-ARGS" == "" ]
        then
          echo "${{vars.MVN-COMPILE-ARGS }}" | tr -d  > "$CLOUDBEES_OUTPUTS/MVN-COMPILE-ARGS"
        fi

        yq '.cb-platform.component.[0].mvn-test-args' ${{ inputs.CONFIG_FILE }} | tr -d '\n' > "$CLOUDBEES_OUTPUTS/MVN-TEST-ARGS"
        if ["$CLOUDBEES_OUTPUTS/MVN-TEST-ARGS" == "" ]
        then
          echo "${{vars.MVN-TEST-ARGS }}" | tr -d  > "$CLOUDBEES_OUTPUTS/MVN-TEST-ARGS"
        fi

        yq '.cb-platform.component.[0].dockerfile' ${{ inputs.CONFIG_FILE }} | tr -d '\n' > "$CLOUDBEES_OUTPUTS/DOCKERFILE"
        if ["$CLOUDBEES_OUTPUTS/DOCKERFILE" == "" ]
        then
          echo "${{vars.CONTEXT }}" | tr -d  > "$CLOUDBEES_OUTPUTS/DOCKERFILE"
        fi

        yq '.cb-platform.component.[0].sq-project-key' ${{ inputs.CONFIG_FILE }} | tr -d '\n' > "$CLOUDBEES_OUTPUTS/SQ-PROJECT-KEY"
        yq '.cb-platform.component.[0].artifact-destination' ${{ inputs.CONFIG_FILE }} | tr -d '\n' > "$CLOUDBEES_OUTPUTS/ARTIFACT-DESTINATION"
        yq '.cb-platform.component.[0].kaniko-build-args' ${{ inputs.CONFIG_FILE }} | tr -d '\n' > "$CLOUDBEES_OUTPUTS/KANIKO-BUILD-ARGS"
        yq '.cb-platform.component.[0].kaniko-labels' ${{ inputs.CONFIG_FILE }} | tr -d '\n' > "$CLOUDBEES_OUTPUTS/KANIKO-LABELS"

```