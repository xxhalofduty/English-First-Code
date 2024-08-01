"""
Carlos Jose Falcon Barrios
William Ensteban Carrero Vasquez
Diego Alejandro Muñoz Ortega
"""
# Definición de los diccionarios para cada opción
options = {
    1: "Operating Systems",
    2: "Photo Software",
    3: "Website Designer",
    4: "Blog Designer",
    5: "Security Software",
    6: "Network Development",
    7: "Games Development",
    8: "Apps Development"
}

details = {
    1: {
        "Linux": "ˈlɪnəks",
        "Windows": "ˈwɪndəʊz",
        "CLI": "siː-ɛl-aɪ",
        "Kernel": "ˈkɜːnᵊl",
        "User Interface": "ˈjuːzər ˈɪntəfeɪs",
        "File System": "faɪl ˈsɪstəm",
        "Process Management": "ˈprəʊsɛs ˈmænɪʤmənt",
        "Multitasking": "ˌmʌltɪˈtɑːskɪŋ",
        "Drivers": "ˌmʌltɪˈtɑːskɪŋ",
        "Virtual Memory": "ˈvɜːʧuəl ˈmɛmᵊri",
        "Permissions": "pəˈmɪʃᵊnz",
        "Scheduling": "ˈʃɛdjuːlɪŋ",
        "Daemons": "ˈdiːmənz",
        "System Calls": "ˈsɪstəm kɔːlz",
        "Patch": "pæʧ"
    },
    
    2: {
        "Photoshop": "ˈfəʊtəʊˌʃɒp",
        "GIMP": "ɡɪmp",
        "Image Editing": "ˈɪmɪʤ ˈɛdɪtɪŋ",
        "Filters": "ˈfɪltəz",
        "Layers": "ˈleɪəz",
        "Masking": "ˈmɑːskɪŋ",
        "Retouching": "ˌriːˈtʌʧɪŋ",
        "Resolution": "ˌrɛzəˈluːʃᵊn",
        "Color Correction": "ˈkʌlə kəˈrɛkʃᵊn",
        "Cropping": "ˈkrɒpɪŋ",
        "Export Formats": "ɛksˈpɔːt ˈfɔːmæts",
        "RAW": "rɔː",
        "Brush Tool": "brʌʃ tuːl",
        "Presets": "prɪˈsɛts",
        "Metadata": "ˈmɛtəˌdeɪtə"
    },
    
    3: {
        "WordPress": "ˈwɜːdˌprɛs",
        "Responsive Design": "rɪˈspɒnsɪv dɪˈzaɪn",
        "Typography": "taɪˈpɒɡrəfi",
        "Color Scheme": "ˈkʌlə skiːm",
        "User Experience": "ˈjuːzər ɪkˈspɪəriəns",
        "Prototyping": "ˈprəʊtətaɪpɪŋ",
        "Layout": "ˈleɪaʊt",
        "CSS Grid": "siː-ɛs-ɛs ɡrɪd",
        "Web Accessibility": "wɛb əkˌsɛsəˈbɪləti",
        "SEO": "ɛs-iː-əʊ",
        "Mockups": "ˈmɒkˈʌps",
        "HTML/CSS": "eɪʧ-tiː-ɛm-ɛl/siː-ɛs-ɛs",
        "JavaScript": "ˈʤɑːvəskrɪpt",
        "Navigation": "ˌnævɪˈɡeɪʃᵊn",
        "Tailwind CSS": "ˈteɪlwɪnd siː-ɛs-ɛs"
    },
    
    4: {
        "Blogger": "ˈblɒɡə",
        "Medium": "ˈmiːdiəm",
        "Ghost": "ɡəʊst",
        "Template": "ˈtɛmplɪt",
        "Content Management System": "ˈkɒntɛnt ˈmænɪʤmənt ˈsɪstəm",
        "Theme": "θiːm",
        "Widgets": "ˈwɪʤɪts",
        "RSS Feed": "ɑːr-ɛs-ɛs fiːd",
        "Post": "pəʊst",
        "Comments": "ˈkɒmɛnts",
        "Header": "ˈhɛdə",
        "Footer": "ˈfʊtə",
        "Social Sharing": "ˈsəʊʃᵊl ˈʃeərɪŋ",
        "Customization": "ˌkʌstəmaɪˈzeɪʃᵊn",
        "Draft": "drɑːft"
    },
    
    5: {
        "Norton": "ˈnɔːtᵊn",
        "Antivirus": "ˌæntiˈvaɪərəs",
        "Firewall": "ˈfaɪəwɔːl",
        "Encryption": "ɪnˈkrɪpʃᵊn",
        "Malware": "ˈmælweə",
        "Phishing Protection": "ˈfɪʃɪŋ prəˈtɛkʃᵊn",
        "Spyware": "ˈspaɪweə",
        "VPN": "viː-piː-ɛn",
        "Intrusion Detection": "ɪnˈtruːʒᵊn dɪˈtɛkʃᵊn",
        "Password Manager": "ˈpɑːswɜːd ˈmænɪʤə",
        "Two-Factor Authentication": "tuː-ˈfæktər ɔːˌθɛntɪˈkeɪʃᵊn",
        "Data Breach": "ˈdeɪtə briːʧ",
        "Cybersecurity": "ˌsaɪbəsɪˈkjʊərəti",
        "Threat Analysis": "θrɛt əˈnæləsɪs",
        "Backup": "ˈbækʌp"
    },
    
    6: {
        "Cisco": "ˈsɪskəʊ",
        "Juniper": "ˈʤuːnɪpə",
        "Protocols": "ˈprəʊtəkɒlz",
        "Router": "ˈruːtə",
        "Switch": "swɪʧ",
        "IP Addressing": "aɪ-piː əˈdrɛsɪŋ",
        "VLAN": "viː-ɛl-eɪ-ɛn",
        "Firewall": "ˈfaɪəwɔːl",
        "Bandwidth": "ˈbændwɪdθ",
        "Latency": "ˈleɪtᵊnsi",
        "NAT": "ɛn-eɪ-tiː",
        "DNS": "diː-ɛn-ɛs",
        "TCP/IP": "tiː-siː-piː/aɪ-piː",
        "Network Topology": "ˈnɛtwɜːk təˈpɒləʤi",
        "Load Balancing": "ləʊd ˈbælᵊnsɪŋ"
    },
    
    7: {
        "Unity": "ˈjuːnəti",
        "Unreal Engine": "ʌnˈrɪəl ˈɛnʤɪn",
        "Game Engine": "ɡeɪm ˈɛnʤɪn",
        "Graphics": "ˈɡræfɪks",
        "Physics Engine": "ˈfɪzɪks ˈɛnʤɪn",
        "Character Design": "ˈkærəktə dɪˈzaɪn",
        "Level Design": "ˈlɛvᵊl dɪˈzaɪn",
        "Sound Design": "saʊnd dɪˈzaɪn",
        "Scripting": "ˈskrɪptɪŋ",
        "Multiplayer": "ˌmʌltɪˈpleɪə",
        "Animation": "ˌænɪˈmeɪʃᵊn",
        "Rendering": "ˈrɛndᵊrɪŋ",
        "Debugging": "diːˈbʌɡɪŋ",
        "Optimization": "ˌɒptɪmaɪˈzeɪʃᵊn",
        "Gameplay": "ˈɡeɪmpleɪ"
    },
    
    8: {
        "Android Studio": "ˈændrɔɪd ˈstjuːdiəʊ",
        "React Native": "riˈækt ˈneɪtɪv",
        "Mobile Platform": "ˈməʊbaɪl ˈplætfɔːm",
        "API": "eɪ-piː-aɪ",
        "Cross-Platform": "krɒs-ˈplætfɔːm",
        "User Interface": "ˈjuːzər ˈɪntəfeɪs",
        "User Experience": "ˈjuːzər ɪkˈspɪəriəns",
        "Backend": "ˌbækˈɛnd",
        "Framework": "ˈfreɪmwɜːk",
        "SDK": "ɛs-diː-keɪ",
        "Agile Development": "ˈæʤaɪl dɪˈvɛləpmənt",
        "Database": "ˈdeɪtəbeɪs",
        "Deployment": "dɪˈplɔɪmənt",
        "Testing": "ˈtɛstɪŋ",
        "App Store": "æp stɔː"
    }
}

# Mostrar las opciones disponibles al usuario
print("Please choose one of the following options:")
for key, value in options.items():
    print(f"{key}. {value}")

# Obtener la opción seleccionada por el usuario
try:
    choice = int(input("Enter the number of your choice: "))
    if choice in details:
        print(f"You have chosen: {options[choice]}")
        # Mostrar las keys del diccionario correspondiente a la opción elegida
        print("\nChoose one of the following keys to view the content:")
        for key in details[choice].keys():
            print(key)
        
        # Obtener la key seleccionada por el usuario
        selected_key = input("\nEnter the key you want to see: ")
        if selected_key in details[choice]:
            print(f"\nContent of {selected_key}: {details[choice][selected_key]}")
        else:
            print("\nInvalid key.")
    else:
        print("\nInvalid option.")
except ValueError:
    print("\nUnvalid entry. Please enter a number.")
