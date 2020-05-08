#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

requirements:
  DockerRequirement:
    dockerPull: "biocontainers/samtools:v1.7.0_cv4"
  InlineJavascriptRequirement: {}

inputs:

  InputFile:
    type: File
    inputBinding:
      position: 100

  Output:
    type: string
    default: "samtoolssortoutput.dat"
    inputBinding:
      position: 99
      prefix: "-o"
      valueFrom: $("samtoolssortoutput.dat")

#OPTIONAL ARGS

  CompressionLevel:
    type: int?
    inputBinding:
      prefix: "-l"

  MaxMemory:
    type: int?
    inputBinding:
      prefix: "-m"

  SortByReadName:
    type: boolean?
    inputBinding:
      prefix: "-n"

  SortByTag:
    type: string?
    inputBinding:
      prefix: "-t"

  TemporaryFilePrefix:
    type: string?
    inputBinding:
      prefix: "-T"

  InputFmtOption:
    type: string[]?
    inputBinding:
      prefix: "--input-fmt-option"

  OutputFmtOption:
    type: string[]?
    inputBinding:
      prefix: "--output-fmt-option"

  Reference:
    type: File?
    inputBinding:
      prefix: "--reference"

  Threads:
    type: int?
    inputBinding:
      prefix: "-@"

  OutputFormat:
    type:
    - "null"
    - type: enum
      symbols:
        - SAM
        - BAM
        - CRAM
    inputBinding:
      prefix: "--output-fmt"


baseCommand: ["samtools"]

arguments:
  - valueFrom: "sort"
    position: -1


outputs:
  alignment:
    type: File
    outputBinding:
      glob: "samtoolssortoutput.dat"




