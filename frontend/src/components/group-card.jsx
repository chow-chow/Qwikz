import {
	Card,
	CardContent,
	CardFooter,
	CardTitle,
	CardDescription,
	CardHeader,
} from '@/components/ui/card'
import Image from 'next/image'

export default function GroupCard() {
	return (
		<Card className='w-[300px]'>
			<Image
				src={'/group-image.jpg'}
				alt='Group Image'
				width={300}
				height={168}
				className='aspect-video object-cover rounded-t-md'
			/>
			<CardHeader>
				<CardTitle>Group Name</CardTitle>
				<CardDescription>Group Description</CardDescription>
			</CardHeader>
		</Card>
	)
}
