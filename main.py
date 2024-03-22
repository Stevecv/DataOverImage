from math import floor

from PIL import Image


def encode(text, image_name):
    im = Image.open(image_name)
    width, height = im.size

    total_pixels = width * height
    text_length = len(text)
    pixel_spacing = floor(total_pixels / text_length)

    if pixel_spacing >= 255:
        pixel_spacing = 255

    meta_color = im.getpixel((0, 0))
    im.putpixel((0, 0), (meta_color[0], meta_color[1], pixel_spacing))

    text_array = list(text)
    pixel_index = 0
    for letter in text_array:
        pixel_index += pixel_spacing
        y = floor(pixel_index / width)
        x = floor(pixel_index % width)

        color = im.getpixel((x, y))
        im.putpixel((x, y), (color[0], color[1], ord(letter)))

    return im


def decode(image_name):
    im = Image.open(image_name)
    pixel_spacing = im.getpixel((0, 0))[2]
    width, height = im.size

    possible_pixels = width*height

    for pixel_index in range(possible_pixels):
        y = floor(pixel_index / width)
        x = floor(pixel_index % width)

        pixel = im.getpixel((x, y))[2]
        print(chr(pixel))



encoded_image = encode("""The British Empire comprised the dominions, colonies, protectorates, mandates, and other territories ruled or administered by the United Kingdom and its predecessor states. It began with the overseas possessions and trading posts established by England in the late 16th and early 17th centuries. At its height in the 19th and early 20th century, it was the largest empire in history and, for a century, was the foremost global power.[1] By 1913, the British Empire held sway over 412 million people, 23 percent of the world population at the time,[2] and by 1920, it covered 35.5 million km2 (13.7 million sq mi),[3] 24 per cent of the Earth's total land area. As a result, its constitutional, legal, linguistic, and cultural legacy is widespread. At the peak of its power, it was described as "the empire on which the sun never sets", as the sun was always shining on at least one of its territories.[4]

During the Age of Discovery in the 15th and 16th centuries, Portugal and Spain pioneered European exploration of the globe, and in the process established large overseas empires. Envious of the great wealth these empires generated,[5] England, France, and the Netherlands began to establish colonies and trade networks of their own in the Americas and Asia. A series of wars in the 17th and 18th centuries with the Netherlands and France left England (Britain, following the 1707 Act of Union with Scotland) the dominant colonial power in North America. Britain became a major power in the Indian subcontinent after the East India Company's conquest of Mughal Bengal at the Battle of Plassey in 1757.

The American War of Independence resulted in Britain losing some of its oldest and most populous colonies in North America by 1783. While retaining control of British North America (now Canada) and territories in and near the Caribbean in the British West Indies, British colonial expansion turned towards Asia, Africa, and the Pacific. After the defeat of France in the Napoleonic Wars (1803–1815), Britain emerged as the principal naval and imperial power of the 19th century and expanded its imperial holdings. It pursued trade concessions in China and Japan, and territory in Southeast Asia. The "Great Game" and "Scramble for Africa" also ensued. The period of relative peace (1815–1914) during which the British Empire became the global hegemon was later described as Pax Britannica (Latin for "British Peace"). Alongside the formal control that Britain exerted over its colonies, its dominance of much of world trade, and of its oceans, meant that it effectively controlled the economies of, and readily enforced its interests in, many regions, such as Asia and Latin America.[6][7] It also came to dominate the Middle East. Increasing degrees of autonomy were granted to its white settler colonies, some of which were formally reclassified as Dominions by the 1920s. By the start of the 20th century, Germany and the United States had begun to challenge Britain's economic lead. Military, economic and colonial tensions between Britain and Germany were major causes of the First World War, during which Britain relied heavily on its empire. The conflict placed enormous strain on its military, financial, and manpower resources. Although the empire achieved its largest territorial extent immediately after the First World War, Britain was no longer the world's preeminent industrial or military power.

In the Second World War, Britain's colonies in East Asia and Southeast Asia were occupied by the Empire of Japan. Despite the final victory of Britain and its allies, the damage to British prestige and the British economy helped accelerate the decline of the empire. India, Britain's most valuable and populous possession, achieved independence in 1947 as part of a larger decolonisation movement, in which Britain granted independence to most territories of the empire. The Suez Crisis of 1956 confirmed Britain's decline as a global power, and the handover of Hong Kong to China on 1 July 1997 symbolised for many the end of the British Empire,[8][9] though fourteen overseas territories that are remnants of the empire remain under British sovereignty. After independence, many former British colonies, along with most of the dominions, joined the Commonwealth of Nations, a free association of independent states. Fifteen of these, including the United Kingdom, retain the same person as monarch, currently King Charles III.""", "TestImage.jpg")

encoded_image.save("EncodedImage.png")


decode("EncodedImage.png")