import json
#json file
lexconfig='''
{
  "alb": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "are": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "arg": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "arm": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "aus": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "poa": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "aut": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "aze": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bel": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bfa": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bgd": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bgr": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bhr": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bhs": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bih": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "blr": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bol": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "mid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bra": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "brn": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "bwa": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "can": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "weaponpermit": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "che": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "chl": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "chn": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "civ": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "cmr": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "cod": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "col": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "cri": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "cze": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "deu": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "dnk": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "dom": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "dza": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "ecu": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "egy": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "esp": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "est": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "fin": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "fra": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "gbr": {
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "geo": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "gha": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "grc": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "gtm": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "hkg": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "hnd": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "hrv": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "hti": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "hun": {
    "ac": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "idn": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "irl": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "psc": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "irq": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "isl": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "isr": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "ita": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "jam": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "jor": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "jpn": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "kaz": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "ken": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "kgz": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "khm": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "kos": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "kwt": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "lka": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "ltu": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "lux": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "lva": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mar": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mda": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mdv": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mex": {
    "cid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "voterid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mkd": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mlt": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mmr": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mne": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "moz": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mus": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "mys": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "ikad": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "mykad": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "mykas": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "mytentera": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "nga": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "voterid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "nic": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "nld": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "nor": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "omn": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "pak": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "pan": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "per": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "phl": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "pid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "postalid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "sss": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "taxid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "umid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "voterid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "pol": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "pri": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "voterid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "prt": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "pry": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "qat": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "rou": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "rus": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "rwa": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "sau": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "sen": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "sgp": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "epass": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "fin": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "spass": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "wp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "slv": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "srb": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "svk": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "svn": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "swe": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "tha": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "tto": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "tun": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "tur": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "twn": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "rp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "tza": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "voterid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "uga": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "ukr": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "ury": {
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "usa": {
    "bcc": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "gc": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "gec": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "nexus": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "vid": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "weaponpermit": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "wp": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "uzb": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "ven": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "vnm": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  },
  "zaf": {
    "dl": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    },
    "id": {
      "supportedSide": [
        "front"
      ],
      "notApplicable": {
        "front": [],
        "back": [],
        "default": []
      },
      "notSupported": {
        "front": [],
        "back": [],
        "default": []
      },
      "isDocumentUploaded": {
        "notApplicable": {
          "front": [],
          "back": []
        },
        "notSupported": {
          "front": [],
          "back": []
        }
      },
      "disableOCR": {
        "front": false
      },
      "useFraasFaceCheck": true,
      "quality": {
        "endpoint": "",
        "params": {
          "face": [
            "faceCheck"
          ]
        }
      },
      "useAddressSplitLambda": true
    }
  }
}'''
#Convert from JSON to Python(parse the json data)
x=json.loads(lexconfig)
#To get the number of countries(keys)in the dictionary
num_countries=len(x)
print("Number of countries",num_countries)
#print(x.keys())
count=0
for i in x:
  y=len(x[i])
  count+=y
print(count)



    



